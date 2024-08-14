# Consultations

A consultation is the process of asking organizations and people for feedback to a draft of a legislative document.

## jolux:Consultation

### URI

The URI of a consultation contains the following parts:

- Namespace and path: `https://fedlex.data.admin.ch/eli/dl/proj/`
- Year with 4 digits
- Arbitrary identifier number
- Task starting with `cons_` for consultation and a running number

Example: `https://fedlex.data.admin.ch/eli/dl/proj/2022/89/cons_1`

### Literals

| Property               | Type of Value  |
| ---------------------- | -------------- |
| jolux:eventTitle       | rdf:langString |
| jolux:eventId          | xsd:string     |
| jolux:eventDescription | rdf:langString |

### Outgoing Relations

| Property                            | Type of Value / Value                                              |
| ----------------------------------- | ------------------------------------------------------------------ |
| jolux:consultationStatus            | one of https://fedlex.data.admin.ch/vocabulary/consultation-status |
| jolux:hasSubTask                    | a jolux:ConsultationTask                                           |
| jolux:foreseenImpactToLegalResource | a jolux:Work from the classified compilation (CC)                  |
| rdfs:type                           | jolux:Consultation                                                 |

### Incoming Relations

| Type of Value | Property           |
| ------------- | ------------------ |
| a jolux:Draft | jolux:draftHasTask |

## jolux:ConsultationTask

The `jolux:ConsultationTask` contains most of the important information from a consultation. Completed consultations contain three different `jolux:ConsultationTask` differentiated by additional classes:

- `jolux:ConsultationPhase` with URI slug `cons-open`
- `jolux:PositionStatementPublication` with URI slug `cons-pos`
- `jolux:ResultOfAConsultationPublication` with URI slug `cons-result`

## jolux:ConsultationPhase

### Literals

| Property             | Type of Value | Description               |
| -------------------- | ------------- | ------------------------- |
| jolux:eventStartDate | xsd:date      | Begin of the consultation |
| jolux:eventEndDate   | xsd:date      | End of the consultation   |

### Outgoing Relations

| Property                                  | Type of Value / Value                                             | Description                     |
| ----------------------------------------- | ----------------------------------------------------------------- | ------------------------------- |
| jolux:institutionInChargeOfTheEvent       | one of https://fedlex.data.admin.ch/vocabulary/legal-institutions |                                 |
| jolux:institutionInChargeOfTheEventLevel2 | one of https://fedlex.data.admin.ch/vocabulary/legal-institutions |                                 |
| jolux:opinionIsAboutDraftDocument         | a jolux:Work                                                      | The subject of the consultation |
| jolux:opinionHasDraftRelatedDocument      | a jolux:Work                                                      | Accompanying documents          |

## jolux:PositionStatementPublication

### Outgoing Relations

| Property                                  | Type of Value / Value                                             | Description               |
| ----------------------------------------- | ----------------------------------------------------------------- | ------------------------- |
| jolux:institutionInChargeOfTheEvent       | one of https://fedlex.data.admin.ch/vocabulary/legal-institutions |                           |
| jolux:institutionInChargeOfTheEventLevel2 | one of https://fedlex.data.admin.ch/vocabulary/legal-institutions |                           |
| jolux:opinionHasDraftRelatedDocument      | a jolux:Work                                                      | All consultation comments |

## jolux:ResultOfAConsultationPublication

### Outgoing Relations

| Property                                  | Type of Value / Value                                             | Description                               |
| ----------------------------------------- | ----------------------------------------------------------------- | ----------------------------------------- |
| jolux:institutionInChargeOfTheEvent       | one of https://fedlex.data.admin.ch/vocabulary/legal-institutions |                                           |
| jolux:institutionInChargeOfTheEventLevel2 | one of https://fedlex.data.admin.ch/vocabulary/legal-institutions |                                           |
| jolux:opinionHasDraftRelatedDocument      | a jolux:Work                                                      | Report on the results of the consultation |

## Visual Representation

:::{figure-md} consultation
![consultation](img/consultation.svg)

Overview of a `jolux:Consultation`
:::

## Useful Queries

### Planned Consultations

The following query reports all the planned consultations:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?consultation WHERE {
 ?consultation jolux:consultationStatus <https://fedlex.data.admin.ch/vocabulary/consultation-status/1>. 
}
```

### Impacted Legal Resources

The following query asks for all the impacted legal resources by currently ongoing consultations:

```sparql
PREFIX jolux: <http://data.legilux.public.lu/resource/ontology/jolux#>
SELECT ?consultation ?resource WHERE {
 ?consultation jolux:consultationStatus <https://fedlex.data.admin.ch/vocabulary/consultation-status/2>.
 ?consultation jolux:foreseenImpactToLegalResource ?resource.
}
```
