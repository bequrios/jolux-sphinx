# Vocabularies

In RDF, a vocabulary is a set of predefined terms, that are used to describe resources. These terms are defined in a way that allows them to be used **consistently across different datasets**.

Fedlex defines and makes use of multiple vocabularies. This sub-page lists the main vocabularies and its associated properties that are used in describing the legal resources.

## Text Types

- URI: https://fedlex.data.admin.ch/vocabulary/resource-type
- Description: The **text types** vocabulary is used to classify the text type of a jolux:Work.
- Predicates: jolux:typeDocument, jolux:historicalTypeDocument

The following SPARQL query shows all the entries of this vocabulary with its labels:

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?term ?label WHERE {
    ?term skos:inScheme <https://fedlex.data.admin.ch/vocabulary/resource-type>;
        skos:prefLabel ?label.
    FILTER NOT EXISTS {?term a skos:Collection}
    FILTER (lang(?label) = "en")
}
```

## Type of the Act

- URI: https://fedlex.data.admin.ch/vocabulary/legal-resource-genre
- Description: The **type of the act** vocabulary is used to classify the type of a jolux:Act.
- Predicates: jolux:legalResourceGenre

The following SPARQL query shows all the entries of this vocabulary with its labels:

```sparql
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?term ?label WHERE {
    ?term skos:inScheme <https://fedlex.data.admin.ch/vocabulary/legal-resource-genre>;
        skos:prefLabel ?label.
    FILTER NOT EXISTS {?term a skos:Collection}
    FILTER (lang(?label) = "en")
}
```