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