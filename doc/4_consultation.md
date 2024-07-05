# Consultation

A consultation is the process of asking organizations and people for feedback to a draft of a legislative document.

All consultations are from type {term}`Consultation` and have a consultation status from the vocabulary https://fedlex.data.admin.ch/vocabulary/consultation-status

The following query asks for the different possible consultation states:

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
SELECT * WHERE {
 <https://fedlex.data.admin.ch/vocabulary/consultation-status> skos:hasTopConcept ?status.
}
```

One of the most important properties of a consultation are the legal resources it will have impact on. These are connected via jolux:foreseenImpactToLegalResource to the consultation:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT * WHERE {
 ?consultation jolux:foreseenImpactToLegalResource ?resource.
} LIMIT 10
```

### Planned Consultations

The following query reports all the consultations with status 1 (planned consultations):

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?consultation WHERE {
 ?consultation jolux:consultationStatus <https://fedlex.data.admin.ch/vocabulary/consultation-status/1>. 
}
```
