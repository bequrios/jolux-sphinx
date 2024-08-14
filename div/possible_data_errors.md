# Possible Errors in Fedlex Data

## jolux:dateApplicability Used Wrongly

This is normally used only on jolux:Consolidation, but the following query gives some others:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT * WHERE {
 ?s jolux:dateApplicability ?date;
    a ?type.
  FILTER NOT EXISTS {?s a jolux:Consolidation}
}
```