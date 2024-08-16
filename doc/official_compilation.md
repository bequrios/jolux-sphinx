# Official Compilation (OC)

The *Official Compilation (OC)* is according to the [lexicon of parliamentary terms](https://www.parlament.ch/en/%C3%BCber-das-parlament/parlamentsw%C3%B6rterbuch/parlamentsw%C3%B6rterbuch-detail?WordId=11#q=official) the compilation of primarily the federal constitution, federal acts and federal decrees.

This part explains all the important objects that build an entry in the OC and it does so with the help of the federal constitution as an example of an entry in the OC.

:::{admonition} Hint for legal laypersons
:class: hint
Entries in the OC do not represent something like a current consolidated version of a legal resource but are some kind of "building blocks" of an actual law text. Updates to a legal text are published as "deltas" to already existing texts - much like an additional commit in software development.

In distinction from the OC, the current consolidated law texts are modelled in the [Classified Compilation](classified_compilation.md).
:::

## Example

Throughout this sub-page, the federal constitution is used as an example of an entry in the OC.

- URI: https://fedlex.data.admin.ch/eli/oc/1999/404
- URL: https://www.fedlex.admin.ch/eli/oc/1999/404
- [Metadata viewer](https://fedlex.data.admin.ch/en-CH/metadata?value=https:%2F%2Ffedlex.data.admin.ch%2Feli%2Foc%2F1999%2F404)

## URI

The URI of an entry in the OC contains the following parts:

- Standard namespace and path: `https://fedlex.data.admin.ch/eli/`
- the part `oc/` denotes the official compilation, meaning that this URI identifies something that is part of the OC of the federal law
- `YYYY/` is the year of the publication
- `ID` an identifier that has no specific meaning

## General Structure

Every entry in the OC is of type jolux:Act.

:::{admonition} jolux:Act
:class: note
:name: Act
The owl:Class **jolux:Act** is used for entries in the Official Compilation and the Federal Gazette. It is of the same [abstraction level](abstraction_levels.md) as [jolux:Work](#Work) and all jolux:Act are also jolux:Work.
:::

For jolux:Act, the additional [abstraction levels](abstraction_levels.md) jolux:Expression and jolux:Manifestation are also available for all entries.

The following figure shows the general structure of an entry in the OC:

:::{figure-md} oc_general
![](img/oc_general.svg)

General structure of an entry in the Official Compilation (CC).
:::

The following SPARQL query shows all the different jolux:Expression for the federal constitution:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?expression WHERE {
    <https://fedlex.data.admin.ch/eli/oc/1999/404> jolux:isRealizedBy ?expression.
}
```

The following SPARQL query shows all the different jolux:Manifestation for the federal constitution:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?manifestation WHERE {
    <https://fedlex.data.admin.ch/eli/oc/1999/404> jolux:isRealizedBy ?expression.
    ?expression jolux:isEmbodiedBy ?manifestation.
}
```

As the jolux:Act is a very abstract representation of a law text, there is e.g. no title of the law attached to the jolux:Act because this is something language specific and therefore added to the [jolux:Expression](#Expression) of the jolux:Act.

## Datatype Properties

- [jolux:publicationDate](#publicationDate)
- [jolux:dateEntryInForce](#dateEntryInForce)
- [jolux:dateDocument](#dateDocument)

## Object Properties

Object properties that point to a vocabulary entry:

- jolux:processType
- [jolux:typeDocument](vocabularies.md#text-types)
- jolux:classifiedByTaxonomyEntry
- [jolux:legalRessourceGenre](vocabularies.md#act-types)
- jolux:responsibilityOf

Object properties that point to an individual:

- [jolux:isRealizedBy](#isRealizedBy)
- jolux:isPartOf

## Additional SPARQL Queries

The following SPARQL query shows all the different jolux:Act that have the legal genre "Basic legislation" and are not yet in force.

```sparql
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?act ?date WHERE {
    ?act jolux:legalResourceGenre <https://fedlex.data.admin.ch/vocabulary/legal-resource-genre/100>;
         jolux:dateEntryInForce ?date.
  FILTER(?date > xsd:date(NOW()))
}
```