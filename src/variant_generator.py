"""Flap variant subclass generator — creates hasPart union expansions in an OWL TBox.

For every class C with ``∃has_part.(A ⊔ B ⊔ …)`` creates:
    C_with_A  ≡  C ⊓ ∃has_part.A
    C_with_B  ≡  C ⊓ ∃has_part.B
and removes the union restriction from C.
"""

from __future__ import annotations

import re
import types as python_types

from owlready2 import Thing, Restriction, Or, SOME, locstr


def generate_variants(
    ontology,
    fma_onto=None,
    has_part=None,
    origin_root=None,
    iri_ns: str = "",
) -> None:
    """Expand hasPart union restrictions into named variant subclasses.

    Parameters
    ----------
    ontology : OWLOntology
        The loaded TBox to extend in place (wound_ontology.owl.OWLOntology).
    fma_onto : OWLOntology, optional
        Loaded FMA TBox for resolving component labels.  Must share the same
        owlready2 World as *ontology* for reliable entity identity.
    has_part : owlready2 ObjectProperty
        The hasPart property object.
    origin_root : owlready2 Class, optional
        If given, only transitive subclasses of this class are expanded.
    iri_ns : str
        IRI prefix for new variant IRIs (e.g. "https://…/OFL/OFLID").
    """
    if has_part is None:
        raise ValueError("has_part (owlready2 property) must be provided")

    onto = ontology.onto
    candidates = (
        _subclasses_of(origin_root) if origin_root is not None
        else list(onto.classes())
    )
    id_counter = [_find_max_id_onto(onto) + 1]

    def new_iri() -> str:
        iri = f"{iri_ns}{id_counter[0]:07d}"
        id_counter[0] += 1
        return iri

    created = 0
    with onto:
        for parent_cls in candidates:
            to_remove = []
            for restr in list(parent_cls.is_a):
                if not isinstance(restr, Restriction):
                    continue
                if restr.property != has_part or restr.type != SOME:
                    continue
                if not isinstance(restr.value, Or):
                    continue

                parent_label = (
                    str(parent_cls.label[0]) if parent_cls.label else parent_cls.name
                )
                flap_base = re.sub(
                    r"\s+flap$", "", parent_label, flags=re.IGNORECASE
                ).strip().lower()

                for comp_cls in restr.value.Classes:
                    comp_label = _owlready2_label(comp_cls, fma_onto)
                    if comp_label.lower() == flap_base:
                        continue

                    variant_label = _make_variant_label(parent_label, comp_label)
                    safe          = _safe_name(variant_label)
                    variant_cls   = python_types.new_class(safe, (Thing,))
                    variant_cls.iri          = new_iri()
                    variant_cls.label        = [locstr(variant_label, "en")]
                    variant_cls.equivalent_to = [parent_cls & has_part.some(comp_cls)]
                    if parent_cls not in variant_cls.is_a:
                        variant_cls.is_a.append(parent_cls)
                    created += 1

                to_remove.append(restr)

            for restr in to_remove:
                parent_cls.is_a.remove(restr)

    ontology._invalidate_caches()
    print(f"[variant_generator] Created {created} variant subclasses.")


# ── Helpers ───────────────────────────────────────────────────────────────────

def _subclasses_of(root_cls) -> list:
    visited: set = set()
    queue = list(root_cls.subclasses())
    while queue:
        cls = queue.pop()
        if cls not in visited:
            visited.add(cls)
            queue.extend(cls.subclasses())
    return list(visited)


def _find_max_id_onto(onto) -> int:
    max_id = 1_000_200
    for ent in onto.classes():
        m = re.search(r"OFLID(\d+)", ent.iri)
        if m:
            max_id = max(max_id, int(m.group(1)))
    return max_id


def _owlready2_label(entity, fma_onto=None) -> str:
    if entity.label:
        return str(entity.label[0])
    if fma_onto is not None:
        other = fma_onto.world.search_one(iri=entity.iri)
        if other and other.label:
            return str(other.label[0])
    return entity.name.replace("_", " ")


def _make_variant_label(parent_label: str, component_label: str) -> str:
    base = re.sub(r"\s+flap$", "", parent_label, flags=re.IGNORECASE).strip()
    return f"{base} flap with {component_label.lower()}"


def _safe_name(name: str) -> str:
    safe = name.strip().replace(" ", "_")
    safe = re.sub(r'[()"/\\:<>\'&@#%?=+,;|]', "", safe)
    safe = re.sub(r"_+", "_", safe).strip("_")
    return safe or "Unknown"
