# Impacts

Impacts is what connect entries in the CC and OC. The entries in the CC are consolidations of entries in the **Official Compilation** (OC). This means that entries in the OC usually have an impact on entries in the CC.

Impacts are modelled as jolux:LegalResourceImpact.

:::{admonition} jolux:LegalResourceImpact
:class: note
:name: LegalResourceImpact
The owl:Class **jolux:LegalResourceImpact** is used to build an entry in the Classified Compilation out of different entries in the Official Compilation. Entries in the Official Compilation have impacts on entries in in the Classified Compilation. The jolux:LegalResourceImpact has two main predicates. jolux:impactFromLegalResource points to the source of the impact and jolux:impactToLegalResource points to the impacted resource.
:::

## Example

Throughout this sub-page, the following jolux:LegalResourceImpact is used as an example.

- URI: https://fedlex.data.admin.ch/eli/oc/2015/104/legal-analysis/LegalResourceImpact/1
- URL: No URL available for jolux:LegalResourceImpact
- [Metadata viewer](https://fedlex.data.admin.ch/de-CH/metadata?value=https:%2F%2Ffedlex.data.admin.ch%2Feli%2Foc%2F2015%2F104%2Flegal-analysis%2FLegalResourceImpact%2F1)

## URI

The URI of a jolux:LegalResourceImpact contains the following parts:

- it starts with the URI of the entry in the Official Compilation that is the source for the impact.
- `/legal-analysis/LegalResourceImpact/` denotes all impacts
- `ID` an identifier that has no specific meaning

## General Structure

The following figure shows the connection between entries in the OC and CC trough jolux:LegalResourceImpact:

:::{figure-md} impact
![](img/impact.svg)

Connection between entries in the Official Compilation and the Classified Compilation through impacts.
:::

As it is shown in the figure above, the connection between jolux:LegalResourceImpact and the entries in the OC and CC is not direct but through an object of class jolux:LegalResourceSubdivision.

:::{admonition} jolux:LegalResourceSubdivision
:class: note
:name: LegalResourceSubdivision
The class **jolux:LegalResourceSubdivision** is used to structure each law text into units: Article (basic unit) and elements above and below this in the hierarchy, as well as annexes and other elements. The concrete unit is attached by using [jolux:legalResourceSubdivisionType](vocabularies.md#subdivision-types).
:::

## Additional SPARQL Queries

The following query shows all the entries in the OC, that have an impact on the federal constitution:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT DISTINCT ?act ?date WHERE {
  ?impact jolux:impactFromLegalResource/jolux:legalResourceSubdivisionIsPartOf ?act;
    jolux:impactToLegalResource/jolux:legalResourceSubdivisionIsPartOf <https://fedlex.data.admin.ch/eli/cc/1999/404>.
  ?act jolux:dateEntryInForce ?date.
} ORDER BY ?date
```