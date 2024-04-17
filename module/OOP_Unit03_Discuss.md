### Discuss which UML models are most applicable at different stages of the SDLC. 

This activity requires us to discuss the appropriate use of Unified Modeling Language (UML) models in different stages of the Software Development Life Cycle (SDLC).

When discussing UML models, we primarily focus on diagrams. According to IBM Documentation (2023), UML models provide an abstract view of the system, while diagrams offer concrete representations of the system.

Rumbaugh, Jacobson, and Booch (2004) provide a brief overview of UML and the diagrams used in different perspectives. Here, I will list the commonly used UML models and when they are most applicable:

#### Static view - Class diagram
The static view provides a logical perspective on the concepts in the application during the design and implementation phases of the SDLC. It assists users in comprehending the system's structure, its components, and their relationships.

Class diagrams are used to represent the primary components of the static view, which are classes and their attributes. They present an overview of the system's structure and facilitate effective communication among developers, which is essential at the foundational stage of the SDLC.

#### Design view - Composite structure diagram
The design view focuses on representing the design structure of an application. It facilitates the mapping of classes to implementation components and helps in expanding high-level classes into a supportive structure.

Composite structure diagrams provide insights into the internal structure of a classifier and the behavior of a collaboration. While they serve a similar purpose as class diagrams, composite structure diagrams allow for a more detailed description of the internal structure of multiple classes and demonstrate their interactions.

#### Use case view - Use case diagram
The use case view is used at the stage of gathering and analyzing requirements to develop a clear structure of the system's requirements and the different actors within the system. It involves describing the interactions between actors and the system as a sequence of messages.

Use case diagrams are used to visually represent these interactions and the different use cases that the system supports. These diagrams illustrate the relationships between actors and use cases, as well as the flow of interactions between them. By using use case diagrams, we can identify the various functionalities or services that the system needs to provide and determine the actors who will interact with it.

#### Activity view - Activity diagram
The activity view focuses on the control and object flow among the steps of a computation or workflow. It represents computational activities involved in performing calculations or workflows. 

Activity diagrams are particularly useful for visualizing workflows, business processes, or the logic of complex algorithms.  It illustrate an action is initiated when the other action is executed, objects and data are available, or certain external events occur.

#### State machine view - State Transition Diagram / State machine diagram
The state machine view is used to depict the potential life cycles of an object belonging to a class. It consists of states connected by transitions, where each state represents a specific period in the object's life, characterized by certain conditions being met.

State machine diagrams are behavioral diagrams that demonstrate the different states an object or system can assume and how it transitions between those states based on events or conditions. These diagrams are particularly useful when modeling systems whose behavior depends on the current state, such as user interfaces or control systems.

#### Interaction view - Sequence diagram
The interaction view illustrates the sequences of message exchanges among the parts of a system and the sequence of interactions between objects over time. It is sometimes used to show the behavioral sequence of a use case.

Sequence diagrams are useful for designing and documenting interactions between different components or objects in the system, especially in scenarios where the timing and order of messages are important. They provide a detailed view of the interactions and collaborations between objects, including the exchange of messages, method invocations, and responses.

#### Deployment view - Deployment diagram
A deployment view is used to assess the consequences of distribution and resource allocation. It illustrates the deployment of runtime artifacts on nodes. Nodes represent runtime resources such as computers or memory, while artifacts are physical implementation units such as files.

Deployment diagrams are used to describe the physical aspects of an object-oriented system. They depict the static deployment view of a system, showcasing the hardware topology and the deployment of runtime artifacts on the nodes.

#### Model management view - Package diagram
Model management consists of packages and dependency relationships among them, which allow a large system to be divided into smaller units. The model comprises a set of packages that hold model elements such as classes, state machines, and use cases.

Package diagrams represent the structure and dependencies between subsystems or modules, providing different views of a system in a multi-tiered application architecture. They can demonstrate the organization of model elements in a large-scale project.
<br>

---

#### References

Fakhroutdinov, K.  The Unified Modeling Language.  Available from: https://www.uml-diagrams.org/ [Accessed 8 April 2024]

IBM Documentation. (2023) UML models and diagrams.  Available from: https://www.ibm.com/docs/en/rational-soft-arch/9.7.0?topic=diagrams-uml-models [Access 15 April 2024] 

Rumbaugh, J., Jacobson, I. & Booch, G. (2004) The Unified Modeling Language Reference Manual. 2nd ed. Boston: Addison-Wesley.  

Visual Paradigm. Overview of the 14 UML Diagram Types.  Available from: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/overview-of-the-14-uml-diagram-types/ [Accessed 15 April 2024]


---

[Return to Module 2 Unit 3](OOP_Unit03.md)
