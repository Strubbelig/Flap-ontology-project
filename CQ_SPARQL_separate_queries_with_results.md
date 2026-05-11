# CQ SPARQL Separate Queries With Results

- Ontology: `ontologies/ofl_2.1.0.ttl`
- Source query catalog: `sparql/cq_questions_answers.sparql`
- Generated: 2026-05-10
- Graph size: 15602 triples

Each section contains one separately runnable SPARQL query followed by the rows returned from `ofl_2.1.0.ttl`. Results use compact CURIE-style IRIs where possible.

## CQ01: What anatomical structures compose the flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?answerClass ?answerLabel
WHERE {
  VALUES ?answerClass { :OFLID10102 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?answerClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?answerClass .
    FILTER(?flap != ?answerClass)
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?answerClass rdfs:label ?answerLabel .
}
ORDER BY ?flapLabel
```


## CQ02: What is the size of the flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?quality ?qualityLabel ?measurement ?value ?unit
WHERE {
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* :OFLID10002 .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* :OFLID10002 .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  OPTIONAL {
    VALUES ?sizeQualityClass { obo:PATO_0000125 obo:PATO_0000128 obo:PATO_0001679 }
    ?flap obo:RO_0000086 ?quality .
    OPTIONAL { ?quality rdf:type/rdfs:subClassOf* ?sizeQualityClass . }
    OPTIONAL { ?quality rdfs:label ?qualityLabel . FILTER(langMatches(lang(?qualityLabel), "en") || lang(?qualityLabel) = "") }
    OPTIONAL {
      ?measurement obo:OBI_0001938 ?quality .
      OPTIONAL { ?measurement obo:IAO_0000004 ?value . }
      OPTIONAL { ?measurement obo:IAO_0000039 ?unit . }
    }
  }
  OPTIONAL { ?flap fma:dimension ?value . }
  OPTIONAL { ?flap fma:has_dimension ?value . }
}
ORDER BY ?flapLabel ?qualityLabel ?value
```



## CQ03: To which vessels is the flap connected?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?answerClass ?answerLabel
WHERE {
  VALUES ?answerClass { :OFLID130000 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?answerClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?answerClass .
    FILTER(?flap != ?answerClass)
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?answerClass rdfs:label ?answerLabel .
}
ORDER BY ?flapLabel
```


## CQ04: What is the Mathes and Nahai classification of the muscle flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?mathesNahaiClass ?mathesNahaiLabel
WHERE {
  VALUES ?mathesNahaiClass { :OFLID10135 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?mathesNahaiClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?mathesNahaiClass .
    FILTER(?flap != ?mathesNahaiClass)
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?mathesNahaiClass rdfs:label ?mathesNahaiLabel .
}
ORDER BY ?flapLabel
```


## CQ05: What is the Nakajima24 classification of the flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?classification ?classificationLabel
WHERE {
  VALUES ?classification {
    :OFLID10075  # Branch-based flap with recognized perforator
    :OFLID10076  # Branch-based flaps
    :OFLID10078  # Perforator based flaps
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?classification .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?classification .
    FILTER(?flap != ?classification)
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?classification rdfs:label ?classificationLabel .
}
ORDER BY ?classificationLabel ?flapLabel
```



## CQ06: Is the flap local, regional or distant?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?distanceClass ?distanceLabel
WHERE {
  VALUES ?distanceClass {
    :OFLID10134  # Local flaps
    :OFLID10140  # Regional flaps
    :OFLID10085  # Distant flaps
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?distanceClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?distanceClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?distanceClass rdfs:label ?distanceLabel .
}
ORDER BY ?distanceLabel ?flapLabel
```


## CQ07: Is the flap pedicled or free?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?connectionClass ?connectionLabel
WHERE {
  VALUES ?connectionClass {
    :OFLID10053  # Flaps with tissue connection to origin / pedicled flaps
    :OFLID10054  # Flaps without tissue connection to origin / free flaps
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?connectionClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?connectionClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?connectionClass rdfs:label ?connectionLabel .
}
ORDER BY ?connectionLabel ?flapLabel
```


## CQ08: Is it a random pattern or an axial or perforator flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?bloodSupplyClass ?bloodSupplyLabel
WHERE {
  VALUES ?bloodSupplyClass {
    :OFLID10004  # Random pattern flaps
    :OFLID10077  # Non-random pattern flaps
    :OFLID10076  # Branch-based flaps
    :OFLID10075  # Branch-based flap with recognized perforator
    :OFLID10078  # Perforator based flaps
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?bloodSupplyClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?bloodSupplyClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?bloodSupplyClass rdfs:label ?bloodSupplyLabel .
}
ORDER BY ?bloodSupplyLabel ?flapLabel
```



## CQ09: Is it a chimeric flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?chimericClass ?chimericLabel
WHERE {
  VALUES ?chimericClass { :OFLID1000092 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?chimericClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?chimericClass .
    FILTER(?flap != ?chimericClass)
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?chimericClass rdfs:label ?chimericLabel .
}
ORDER BY ?flapLabel
```


## CQ10: What is the arterial flow direction, e.g. reversed flow or flow through flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?flowClass ?flowLabel
WHERE {
  VALUES ?flowClass {
    :OFLID10113  # Flaps with anterograde blood flow
    :OFLID10123  # Flaps with retrograde blood flow
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?flowClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?flowClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?flowClass rdfs:label ?flowLabel .
}
ORDER BY ?flowLabel ?flapLabel
```


## CQ11: Is it a rotational, advancement or transpositional flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?movementClass ?movementLabel
WHERE {
  VALUES ?movementClass {
    :OFLID10014  # Rotation flaps
    :OFLID10067  # Transposition flaps
    :OFLID10070  # Advancement flaps
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?movementClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?movementClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?movementClass rdfs:label ?movementLabel .
}
ORDER BY ?flapLabel
```



## CQ12: Is it an island flap?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?islandClass ?islandLabel
WHERE {
  VALUES ?islandClass { :OFLID10115 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?islandClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?islandClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?islandClass rdfs:label ?islandLabel .
}
ORDER BY ?flapLabel
```



## CQ13: How was the insertion site prepared?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?preparationClass ?preparationLabel
WHERE {
  VALUES ?preparationClass { :OFLID130001 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?preparationClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?preparationClass .
    FILTER(?flap != ?preparationClass)
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?preparationClass rdfs:label ?preparationLabel .
}
ORDER BY ?flapLabel
```



## CQ14: Was the flap modified before harvesting?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?preHarvestClass ?preHarvestLabel
WHERE {
  VALUES ?preHarvestClass {
    :OFLID10130  # Flaps without preharvest modification
    :OFLID10131  # Flaps with preharvest modification
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?preHarvestClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?preHarvestClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?preHarvestClass rdfs:label ?preHarvestLabel .
}
ORDER BY ?preHarvestLabel ?flapLabel
```



## CQ15: Did the flap require split-thickness skin grafting?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?skinGraftClass ?skinGraftLabel
WHERE {
  VALUES ?skinGraftClass { :OFLID120066 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?skinGraftClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?skinGraftClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?skinGraftClass rdfs:label ?skinGraftLabel .
}
ORDER BY ?flapLabel
```


## CQ16: How was vessel anastomosis performed?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?anastomosisClass ?anastomosisLabel
WHERE {
  VALUES ?anastomosisClass { :OFLID10223 }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf+ ?anastomosisClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf+ ?anastomosisClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?anastomosisClass rdfs:label ?anastomosisLabel .
}
ORDER BY ?flapLabel
```


## CQ17: Did the flap fully survive?

```sparql
PREFIX : <https://purl.bioontology.org/ontology/OFL/>
PREFIX obo: <http://purl.obolibrary.org/obo/>
PREFIX fma: <http://purl.org/sig/ont/fma/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

# Notes:
# - Each query can be run separately.
# - The first UNION branch supports ABox individuals with asserted or inferred rdf:type.
# - The second UNION branch supports classes in the OFL TBox.
# - For complete answers, run these over a reasoned graph/materialized subclass hierarchy.

SELECT DISTINCT ?flap ?flapLabel ?survivalClass ?survivalLabel
WHERE {
  VALUES ?survivalClass {
    :OFLID10184  # Flaps without tissue loss
    :OFLID10179  # Flaps with loss at the apex
    :OFLID10183  # Flaps with total loss
    :OFLID10180  # Flaps with arterial obstruction
    :OFLID10181  # Flaps with venous obstruction
  }
  {
    ?flap rdf:type ?directType .
    ?directType rdfs:subClassOf* ?survivalClass .
  }
  UNION
  {
    ?flap rdf:type owl:Class ;
          rdfs:subClassOf* ?survivalClass .
  }
  OPTIONAL { ?flap rdfs:label ?flapLabel . FILTER(langMatches(lang(?flapLabel), "en") || lang(?flapLabel) = "") }
  ?survivalClass rdfs:label ?survivalLabel .
}
ORDER BY ?survivalLabel ?flapLabel
```
