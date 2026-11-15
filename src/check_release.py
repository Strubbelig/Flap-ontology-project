"""Pre-release checks for an OFL OWL file.

Run before every release:

    python src/check_release.py ontologies/ofl_2.2.0.owl

Checks
  1. Orphaned blank nodes: anonymous nodes that nothing refers to and that are
     not a legitimate top-level OWL construct (GCI, AllDisjointClasses, annotated
     axiom, ...). In 2.1.0 these were 118 leftover owl:minQualifiedCardinality
     fragments (JOWS review, comment 2.7).
  2. 'min 0' restrictions, which constrain nothing (comment 2.6).
  3. OWL/RDF/RDFS/XSD vocabulary declared as a property or class, e.g.
     owl:minQualifiedCardinality declared as an annotation property.
  4. versionIRI present and, if the file name carries a version, matching it.

Exits with status 1 if any check fails.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import rdflib
from rdflib import OWL, RDF, RDFS, XSD, BNode, Literal, URIRef

# rdf:type values that may legitimately sit on a top-level blank node
ROOT_TYPES = {OWL.AllDisjointClasses, OWL.AllDifferent, OWL.AllDisjointProperties,
              OWL.NegativePropertyAssertion, OWL.Axiom, OWL.Annotation}
# predicates that make a top-level blank class expression a general class axiom
GCI_PREDICATES = {RDFS.subClassOf, OWL.equivalentClass, OWL.disjointWith}
RESERVED = (str(OWL), str(RDF), str(RDFS), str(XSD))
DECLARATION_TYPES = {OWL.AnnotationProperty, OWL.ObjectProperty, OWL.DatatypeProperty, OWL.Class}


def orphaned_blank_nodes(g: rdflib.Graph) -> list[BNode]:
    referenced = {o for o in g.objects() if isinstance(o, BNode)}
    orphans = []
    for s in {s for s in g.subjects() if isinstance(s, BNode)}:
        if s in referenced:
            continue
        if set(g.objects(s, RDF.type)) & ROOT_TYPES:
            continue
        if set(g.predicates(s)) & GCI_PREDICATES:
            continue
        orphans.append(s)
    return orphans


def min_zero_restrictions(g: rdflib.Graph) -> list[BNode]:
    found = []
    for p in (OWL.minQualifiedCardinality, OWL.minCardinality):
        for s, o in g.subject_objects(p):
            if isinstance(o, Literal) and str(o).strip() == "0" and (s, RDF.type, OWL.Restriction) in g:
                found.append(s)
    return found


def reserved_declarations(g: rdflib.Graph) -> list[tuple[URIRef, URIRef]]:
    return [(s, t) for t in DECLARATION_TYPES for s in g.subjects(RDF.type, t)
            if isinstance(s, URIRef) and str(s).startswith(RESERVED)]


def version_problems(g: rdflib.Graph, path: Path) -> list[str]:
    versions = [str(v) for v in g.objects(None, OWL.versionIRI)]
    if not versions:
        return ["no owl:versionIRI"]
    m = re.search(r"(\d+\.\d+\.\d+)", path.name)
    if m and not any(v.rstrip("/").endswith(m.group(1)) for v in versions):
        return [f"versionIRI {versions} does not match file name version {m.group(1)}"]
    return []


def owner_label(g: rdflib.Graph, node) -> str:
    """Label of the named class a blank restriction belongs to, if any."""
    seen = set()
    while isinstance(node, BNode) and node not in seen:
        seen.add(node)
        parents = list(g.subjects(None, node))
        if not parents:
            return "(no owner)"
        node = parents[0]
    return str(g.value(node, RDFS.label) or node)


def main(path_str: str) -> int:
    path = Path(path_str)
    g = rdflib.Graph()
    g.parse(path, format="xml" if path.suffix in {".owl", ".rdf"} else None)
    failed = False

    orphans = orphaned_blank_nodes(g)
    print(f"Orphaned blank nodes: {len(orphans)}")
    for b in orphans[:10]:
        print("   ", [(str(p).rsplit('#', 1)[-1], str(o)) for p, o in g.predicate_objects(b)])
    failed |= bool(orphans)

    zeros = min_zero_restrictions(g)
    print(f"'min 0' restrictions: {len(zeros)}")
    for r in zeros[:10]:
        print("    on", owner_label(g, r))
    failed |= bool(zeros)

    reserved = reserved_declarations(g)
    print(f"Reserved vocabulary declared as property/class: {len(reserved)}")
    for s, t in reserved:
        print(f"    {s} declared as {t}")
    failed |= bool(reserved)

    vp = version_problems(g, path)
    print(f"Version IRI: {'ok' if not vp else '; '.join(vp)}")
    failed |= bool(vp)

    print("FAILED" if failed else "All release checks passed.")
    return 1 if failed else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: python src/check_release.py <ontology.owl>")
    sys.exit(main(sys.argv[1]))
