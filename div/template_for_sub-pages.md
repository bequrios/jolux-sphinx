# Title

Summary

## Example

Throughout this sub-page, the following ... is used as an example.

- URI:
- URL:
- [Metadata viewer]()

## URI

## General Structure

Figure with all elements either explained or linked to.

## Datatype Properties

## Object Properties

- [jolux:legalResourceSubdivisionType](vocabularies.md#subdivision-types)
- [jolux:legalResourceSubdivisionIsPartOf](#legalResourceSubdivisionIsPartOf)

## SPARQL Examples

The following query shows all the subdivisions of the federal constitution in the CC with its types:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT * WHERE {
  ?subdivison jolux:legalResourceSubdivisionIsPartOf <https://fedlex.data.admin.ch/eli/cc/1999/404>;
    jolux:legalResourceSubdivisionType ?type.
}
```