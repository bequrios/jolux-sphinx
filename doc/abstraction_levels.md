# Abstraction Levels

In JOLux, all the different legislative resources are always described through different levels of abstraction.

## Work, Expression and Manifestation

The main levels of abstraction in JOLux are:

- [jolux:Work](#Work)
- [jolux:Expression](#Expression)
- [jolux:Manifestation](#Manifestation)

:::{admonition} jolux:Work
:class: note
:name: Work
The owl:Class **jolux:Work** is a general abstraction for all the different legal resources in JOLux. All the objects with type jolux:Work have additional types set to differentiate between the diverse legal resources. As it is a general abstraction, the jolux:Work is language and file-format agnostic.
:::

:::{admonition} jolux:Expression
:class: note
:name: Expression
The owl:Class **jolux:Expression** is a language specific representation of a jolux:Work. The jolux:Expression is file-format agnostic.
:::

:::{admonition} jolux:Manifestation
:class: note
:name: Manifestation
The owl:Class **jolux:Manifestation** is a file-format specific representation of a jolux:Expression entity. So an jolux:Manifestation is a language and file-format specific representation of a jolux:Work.
:::

So basically, [jolux:Work](#Work), [jolux:Expression](#Expression) and [jolux:Manifestation](#Manifestation) always come together to form a rich representation of a legal resource. The vocabulary used to connect these abstraction levels is shown in the following figure:

:::{figure-md} wem
![](img/wem.svg)

Relation between jolux:Work, jolux:Expression und jolux:Manifestation.
:::