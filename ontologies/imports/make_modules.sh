#!/bin/bash
# Builds the OBI and RO import modules of OFL 2.2.1 with ROBOT (SLME, BOT method):
# every axiom of OBI / RO needed for the OFL terms listed in obi_terms.txt / ro_terms.txt.
cd "$(dirname "$0")"
IMP="../../../../Import ontologies"
ROBOT="$HOME/robot/robot.jar"
for name in obi ro; do
  src="$IMP/$name.owl"
  ver=$(grep -m1 -o 'owl:versionIRI rdf:resource="[^"]*"' "$src" | sed 's/.*resource="//; s/"$//')
  java -jar "$ROBOT" extract --method BOT --input "$src" --term-file ${name}_terms.txt \
    annotate --ontology-iri "https://purl.bioontology.org/ontology/OFL/imports/${name}_import.owl" \
             --version-iri "https://purl.bioontology.org/ontology/OFL/2.2.1/imports/${name}_import.owl" \
             --link-annotation http://purl.org/dc/terms/source "$ver" \
    --output ${name}_import.owl || { echo "FAILED: $name"; exit 1; }
  echo "$name module: $(grep -c '<owl:Class rdf:about' ${name}_import.owl) classes, $(grep -c '<owl:ObjectProperty rdf:about' ${name}_import.owl) object properties (source $ver)"
done
