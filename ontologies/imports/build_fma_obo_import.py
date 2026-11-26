"""Build imports/fma_obo_import.owl, the module of the OBO FMA that OFL imports.

Usage:
    python build_fma_obo_import.py FMA_OBO_OWL OFL_OWL OUTPUT_OWL

FMA_OBO_OWL is the OBO version of the FMA (fma_obo.owl, ontology IRI
http://purl.obolibrary.org/obo/fma.owl, release 2020-04-13). The module holds
the FMA classes that OFL references, closed under their named superclasses and
under the classes they are part_of (regional, constitutional, systemic) or
branch_of. For these classes it copies, unchanged, the labels, definitions,
named subClassOf axioms and the part_of / branch_of restrictions, plus the
FMA OBO object properties part_of, regional_part_of, constitutional_part_of,
systemic_part_of and branch_of. Other FMA relations (bounds, attaches_to) are
left out. OFL itself makes fma#part_of and fma#branch_of subproperties of
'Ofl part of' (OFLID13297).
"""
import re
import sys
from xml.sax.saxutils import escape

import pyoxigraph as ox

FMA_OBO, OFL, OUT = sys.argv[1:4]
OBO = "http://purl.obolibrary.org/obo/"
F = OBO + "fma#"
PROPS = ["part_of", "regional_part_of", "constitutional_part_of", "systemic_part_of", "branch_of"]
PART = {F + p for p in PROPS}
SC = "<http://www.w3.org/2000/01/rdf-schema#subClassOf>"
OWL = "http://www.w3.org/2002/07/owl#"

st = ox.Store()
with open(FMA_OBO, "rb") as f:
    st.bulk_load(f, ox.RdfFormat.RDF_XML)

up, rel = {}, {}
for r in st.query(f"SELECT ?c ?s WHERE {{ ?c {SC} ?s FILTER(isIRI(?s)) }}"):
    up.setdefault(r[0].value, set()).add(r[1].value)
for r in st.query(f"SELECT ?c ?p ?v WHERE {{ ?c {SC} ?r . ?r <{OWL}onProperty> ?p ; <{OWL}someValuesFrom> ?v FILTER(isIRI(?v)) }}"):
    rel.setdefault(r[0].value, []).append((r[1].value, r[2].value))
lab = {r[0].value: r[1].value for r in st.query("SELECT ?c ?l WHERE { ?c <http://www.w3.org/2000/01/rdf-schema#label> ?l }")}
dfn = {r[0].value: r[1].value for r in st.query(f"SELECT ?c ?d WHERE {{ ?c <{OBO}IAO_0000115> ?d }}")}

sig = set(re.findall(r"http://purl\.obolibrary\.org/obo/FMA_\d+", open(OFL, encoding="utf-8").read()))
closure, todo = set(), list(sig)
while todo:
    c = todo.pop()
    if c in closure:
        continue
    closure.add(c)
    todo += list(up.get(c, ()))
    todo += [v for p, v in rel.get(c, ()) if p in PART]
n_rel = sum(1 for c in closure for p, v in rel.get(c, ()) if p in PART)

IRI = "https://purl.bioontology.org/ontology/OFL/imports/fma_obo_import.owl"
o = [
    '<?xml version="1.0"?>',
    '<rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#" xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#" xmlns:owl="http://www.w3.org/2002/07/owl#" xmlns:obo="http://purl.obolibrary.org/obo/" xmlns:dcterms="http://purl.org/dc/terms/">',
    f'    <owl:Ontology rdf:about="{IRI}">',
    '        <owl:versionIRI rdf:resource="https://purl.bioontology.org/ontology/OFL/2.2.1/imports/fma_obo_import.owl"/>',
    '        <dcterms:source rdf:resource="http://purl.obolibrary.org/obo/fma/releases/2020-04-13/fma.owl"/>',
    "        <dcterms:title>FMA OBO import module for OFL</dcterms:title>",
    f"        <rdfs:comment>Module of the OBO version of the FMA (fma_obo.owl, ontology IRI http://purl.obolibrary.org/obo/fma.owl, release 2020-04-13; not the original FMA, http://purl.org/sig/ont/fma.owl) for OFL 2.2.1: the {len(sig)} FMA classes referenced by OFL, closed under their named superclasses and the classes they are part_of (regional, constitutional, systemic) or branch_of ({len(closure)} classes), with labels, definitions, the subClassOf axioms between them and their {n_rel} part_of and branch_of restrictions, and the FMA OBO object properties {', '.join(PROPS)}. Axioms are copied unchanged; other FMA relations (bounds, attaches_to) are not included.</rdfs:comment>",
    "    </owl:Ontology>",
    '    <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/title"/>',
    '    <owl:AnnotationProperty rdf:about="http://purl.org/dc/terms/source"/>',
    '    <owl:AnnotationProperty rdf:about="http://purl.obolibrary.org/obo/IAO_0000115"><rdfs:label>definition</rdfs:label></owl:AnnotationProperty>',
]
for p in PROPS:
    o.append(f'    <owl:ObjectProperty rdf:about="{F}{p}">')
    o.append(f"        <rdfs:label>{p}</rdfs:label>")
    if p == "part_of":
        o.append('        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#TransitiveProperty"/>')
    if p in ("regional_part_of", "constitutional_part_of", "systemic_part_of"):
        o.append(f'        <rdfs:subPropertyOf rdf:resource="{F}part_of"/>')
    o.append("    </owl:ObjectProperty>")
for c in sorted(closure, key=lambda x: int(x.rsplit("_", 1)[1])):
    o.append(f'    <owl:Class rdf:about="{c}">')
    if c in lab:
        o.append(f"        <rdfs:label>{escape(lab[c])}</rdfs:label>")
    if c in dfn:
        o.append(f"        <obo:IAO_0000115>{escape(dfn[c])}</obo:IAO_0000115>")
    for s in sorted(up.get(c, ())):
        o.append(f'        <rdfs:subClassOf rdf:resource="{s}"/>')
    for p, v in sorted(x for x in rel.get(c, ()) if x[0] in PART):
        o.append(f'        <rdfs:subClassOf><owl:Restriction><owl:onProperty rdf:resource="{p}"/><owl:someValuesFrom rdf:resource="{v}"/></owl:Restriction></rdfs:subClassOf>')
    o.append("    </owl:Class>")
o.append("</rdf:RDF>")
with open(OUT, "w", encoding="utf-8") as f:
    f.write("\n".join(o) + "\n")
print(f"{len(sig)} FMA classes in OFL, {len(closure)} in the module, {n_rel} part_of/branch_of restrictions")
