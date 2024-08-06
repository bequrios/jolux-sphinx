# Classified Compilation (CC)

The *classified compilation (CC)* (also known as systematic compilation) is according to the [lexicon of parliamentary terms](https://www.parlament.ch/en/%C3%BCber-das-parlament/parlamentsw%C3%B6rterbuch/parlamentsw%C3%B6rterbuch-detail?WordId=216) a regularly updated and revised collection of the law texts of the official compilation.

This part explains all the important objects that build an entry in the CC and it does so with the help of the federal constitution.

## jolux:ConsolidationAbstract

Every entry in the CC is of type jolux:ConsolidationAbstract. The term abstract is not so much meant as a summary but as an abstraction.

### URI

The URI of an entry in the CC contains the following parts:

* Namespace and path: `https://fedlex.data.admin.ch/` is the namespace for all federal legislative information.
* `eli/` stands for [European Legislation Identifier](https://op.europa.eu/en/web/eu-vocabularies/eli) and is a effort to make legislation meta data available in a standardized format.
* the part `cc/` denotes the classified compilation, meaning that this URI identifies something that is part of the classified compilation of the federal law.
* `YYYY/` is the year of the publication.
* `ID` some random identifier that has no specific meaning.

Example: The full URI of the federal constitution is `https://fedlex.data.admin.ch/eli/oc/1999/404`. There is some irony in the federal constitution having the same identifier as the [HTTP 404 error](https://en.wikipedia.org/wiki/HTTP_404).

This URI can be found on the website of [Fedlex](https://www.fedlex.admin.ch/) through a search. If this URI is put into a webbrowser, there is a redirection to https://www.fedlex.admin.ch/eli/oc/1999/404 but this is not the URI of the federal constitution but a website presenting the constitution with some additional meta data.

## Work, Expression, Manifestation

Let's examine the classes of the constitutions URI through the following SPARQL query:

```sparql
SELECT DISTINCT * WHERE {
	<https://fedlex.data.admin.ch/eli/oc/1999/404> a ?class.
}
```

The result shows, that the constitution is something of type `jolux:Work` (besides others). A `jolux:Work` is basically the abstract representation of a law text. Is there a connection to an `jolux:Expression`? Let's find out:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>

SELECT DISTINCT * WHERE {
	<https://fedlex.data.admin.ch/eli/oc/1999/404> ?p ?o.
	?o a jolux:Expression.
}
```

So there are three `jolux:Expression`s connected via `jolux:isRealizedBy`:

* `https://fedlex.data.admin.ch/eli/oc/1999/404/de`
* `https://fedlex.data.admin.ch/eli/oc/1999/404/fr`
* `https://fedlex.data.admin.ch/eli/oc/1999/404/it`

So, a `jolux:Expression` is a **language specific** representation of a `jolux:Work`. The connection to the `jolux:Manifestation` for one expression is queried now:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>

SELECT DISTINCT * WHERE {
	<https://fedlex.data.admin.ch/eli/oc/1999/404/de> ?p ?o.
	?o a jolux:Manifestation.
}
```

resulting in three `jolux:Manifestation`s connected via `jolux:isEmbodiedBy`:

* `https://fedlex.data.admin.ch/eli/oc/1999/404/de/doc`
* `https://fedlex.data.admin.ch/eli/oc/1999/404/de/pdf-a`
* `https://fedlex.data.admin.ch/eli/oc/1999/404/de/pdf-x`

This means that a `jolux:Manifestation` is a **language and file format specific** representation of a `jolux:Work`. If one wants to get e.g. the PDF document of the federal constitution in German, the following query helps:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>

SELECT DISTINCT ?url WHERE {
  <https://fedlex.data.admin.ch/eli/oc/1999/404> jolux:isRealizedBy ?expression.
  ?expression jolux:language <http://publications.europa.eu/resource/authority/language/DEU>;
              jolux:isEmbodiedBy ?manifestation.
  ?manifestation jolux:userFormat <https://fedlex.data.admin.ch/vocabulary/user-format/pdf-a>;
                 jolux:isExemplifiedBy ?url.
}
```

So, the general connection between {term}`Work`, {term}`Expression` and {term}`Manifestation` is shown in the following image:

:::{figure-md} wem
![Work_Expression_Manifestation](img/work_expression_manifestation.svg "Work_Expression_Manifestation")

Relation between jolux:Work, jolux:Expression und jolux:Manifestation.
:::

:::{mermaid}
%%{init: {'theme': 'neutral'}}%%
flowchart TD
    Work(jolux:Work)
    Expression(jolux:Expression)
    Manifestation(jolux:Manifestation)
    Work-->|jolux:isRealizedBy| Expression
    Expression --> |jolux:isEmbodiedBy| Manifestation
    Manifestation --> |jolux:isExemplifiedBy| File[File URL]

    linkStyle default stroke-width:1;
:::
