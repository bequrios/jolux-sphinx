# Classified Compilation (CC)

The *classified compilation (CC)* (also known as systematic compilation) is according to the [lexicon of parliamentary terms](https://www.parlament.ch/en/%C3%BCber-das-parlament/parlamentsw%C3%B6rterbuch/parlamentsw%C3%B6rterbuch-detail?WordId=216) a regularly updated and revised collection of the law texts of the official compilation arranged under subject headings.

This part explains all the important objects that build an entry in the CC and it does so with the help of the federal constitution as an example of an entry in the CC.

:::{admonition} Hint for legal laypersons
:class: hint
Entries in the CC are consolidations of entries in the OC. The main reason for having a Classified Compilation is a better usability of the law texts because the classified compilation represents the current state of a law text.

It is important to realize that the CC is not legally binding, the source of the "true law" is always the OC.
:::

## Example

Throughout this sub-page, the federal constitution is used as an example of an entry in the CC.

- URI: https://fedlex.data.admin.ch/eli/cc/1999/404
- URL: https://www.fedlex.admin.ch/eli/cc/1999/404
- [Metadata viewer](https://fedlex.data.admin.ch/en-CH/metadata?value=https:%2F%2Ffedlex.data.admin.ch%2Feli%2Fcc%2F1999%2F404)

## URI

The URI of an entry in the CC contains the following parts:

- Standard namespace and path: `https://fedlex.data.admin.ch/eli/`
- the part `cc/` denotes the classified compilation, meaning that this URI identifies something that is part of the CC of the federal law
- `YYYY/` is the year of the publication
- `ID` an identifier that has no specific meaning

## General Structure

Every entry in the CC is of type jolux:ConsolidationAbstract.

:::{admonition} jolux:ConsolidationAbstract
:class: note
:name: ConsolidationAbstract
The owl:Class **jolux:ConsolidationAbstract** is used for entries in the Classified Compilation.

It is a consolidation because it consolidates different entries from the OC into a single document that shows the current state. The term *abstract* is not so much meant as a summary but as an abstraction.
:::

A jolux:ConsolidationAbstract has a jolux:Expression attached for representing the title and abbreviation in different languages of this consolidation because this does not change. But there are no jolux:Manifestation these only exist for jolux:Consolidation.

:::{admonition} jolux:Consolidation
:class: note
:name: Consolidation
The owl:Class **jolux:Consolidation** is used for versions that represent a jolux:ConsolidationAbstract at a specific time. It is of the same [abstraction level](abstraction_levels.md) as [jolux:Work](#Work) and all jolux:Consolidation are also jolux:Work.

The different jolux:Consolidation are no "deltas" of the changes but always the complete state a the specific point in time.
:::

For jolux:Consolidation, the additional [abstraction levels](abstraction_levels.md) jolux:Expression and jolux:Manifestation are also available for all entries.

The connection between jolux:Consolidation and jolux:ConsolidationAbstract is made with jolux:isMemberOf.

:::{admonition} jolux:isMemberOf
:class: note
:name: isMemberOf
The object property **jolux:isMemberOf** is used to connect a [jolux:Consolidation](#Consolidation) to a [jolux:ConsolidationAbstract](#ConsolidationAbstract)
:::

The following figure shows the general structure of an entry in the CC:

:::{figure-md} cc_general
![](img/cc_general.svg)

General structure of an entry in the Classified Compilation (CC).
:::

## Datatype Properties

### jolux:ConsolidationAbstract

- [jolux:dateEntryInForce](#dateEntryInForce)
- [jolux:dateDocument](#dateDocument)

### jolux:Consolidation

- [jolux:publicationDate](#publicationDate)
- [jolux:dateApplicability](#dateApplicability)

## Object Properties

### jolux:ConsolidationAbstract

Object properties that point to a vocabulary entry:

- [jolux:typeDocument](vocabularies.md#text-types)
- jolux:classifiedByTaxonomyEntry
- jolux:inForceStatus

Object properties that point to an individual:

- jolux:basicAct
- [jolux:isRealizedBy](#isRealizedBy)

### jolux:Consolidation

Object properties that point to an individual:

- [jolux:isMemberOf](#isMemberOf)
- [jolux:isRealizedBy](#isRealizedBy)

## Additional SPARQL Queries

The following SPARQL query shows all the different versions of the federal constitution:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT * WHERE {
	?consolidation jolux:isMemberOf <https://fedlex.data.admin.ch/eli/cc/1999/404>.
}
```

The following SPARQL query gives the PDF link to the latest version of the constitution in English through a chain to jolux:Consolidation, jolux:Expression and jolux:Manifestation:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT * WHERE {
	?work jolux:isMemberOf <https://fedlex.data.admin.ch/eli/cc/1999/404>;
                jolux:dateApplicability ?date;
                jolux:isRealizedBy ?expression.
  ?expression jolux:language <http://publications.europa.eu/resource/authority/language/ENG>;
              jolux:isEmbodiedBy ?manifestation.
  ?manifestation jolux:format <http://publications.europa.eu/resource/authority/file-type/PDF>;
                 jolux:isExemplifiedBy ?url.
} ORDER BY DESC(?date)
LIMIT 1
```