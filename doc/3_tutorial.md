# Tutorial

This tutorial guides through the basics of the JOLux ontology using the federal constitution as an example.

## URI

The URI of the federal constitution is `https://fedlex.data.admin.ch/eli/oc/1999/404`. This URI has some important information encoded:

* the part `fedlex.data.admin.ch` is the namespace for all federal legislative information.
* `/eli` stands for [European Legislation Identifier](https://op.europa.eu/en/web/eu-vocabularies/eli) and is a effort to make legislation meta data available in a standardized format.
* the part `/oc` denotes the **Official Compilation**, meaning that this URI identifies something that is part of the official compilation of the federal law. The official compilation basically is the sum of the law.
* `/1999` is the year of the publication.
* `/404` is some random identifier that has no specific meaning (there is some irony in the federal constitutions having [HTTP 404 error](https://en.wikipedia.org/wiki/HTTP_404) as identifier).

This URI can be found on the website of [Fedlex](https://www.fedlex.admin.ch/) through a search. If this URI is put into a webbrowser, there is a redirection to https://www.fedlex.admin.ch/eli/oc/1999/404 but this is not the URI of the federal constitution but a website presenting the constitution with some additional meta data.

## JOLux Classes

Let's examine the classes of the constitutions URI through the following SPARQL query:

```{sparql-query}
SELECT DISTINCT * WHERE {
	<https://fedlex.data.admin.ch/eli/oc/1999/404> a ?class
}
```

```SPARQL
SELECT DISTINCT * WHERE {
	<https://fedlex.data.admin.ch/eli/oc/1999/404> a ?class
}
```

The result shows, that the constitution is something of type `jolux:Work` (besides others). A `jolux:Work` is basically the abstract representation of a law text.