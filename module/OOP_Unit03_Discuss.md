### Discuss which UML models are most applicable at different stages of the SDLC. 

This activity requires us to discuss the appropriate use of Unified Modeling Language (UML) models in different stages of the Software Development Life Cycle (SDLC). The choice of UML models depends on the specific stage of the SDLC and the information that needs to be conveyed.

When discussing UML models, we primarily focus on diagrams. According to IBM Documentation (2023), UML models provide an abstract view of the system, while diagrams offer concrete representations of the system.

Rumbaugh, Jacobson, and Booch (2004) provide a brief overview of UML and the diagrams used in different perspectives. Here, I will list the commonly used UML models and when they are most applicable:

#### Static view - Class diagram
The static view is the foundation of UML.  It provides a logical perspective on the concepts in the application during the design and implementation phases of SDLC. It assists users in comprehending the system's structure, its components, and their relationships. The primary components of the static view are classes and their attributes which are represented in class diagrams. 

Class diagrams play a crucial role in designing the software architecture and establishing the groundwork for object-oriented programming (OOP). They present an overview of the system's structure and facilitate effective communication among developers.

#### Design view - Composite structure diagram
The design view focuses on representing the design structure of an application. It facilitates the mapping of classes to implementation components and helps in expanding high-level classes into a supportive structure.  

Composite structure diagram provides insights into the internal structure of a classifier and the behavior of a collaboration. While it serves a similar purpose as a class diagram, the composite structure diagram allows for a more detailed description of the internal structure of multiple classes and demonstrates their interactions.
   
#### Use case view - Use case diagram
The use case view is utilized during the stage of gathering and analyzing requirements to develop a clear understanding of the system's requirements and the roles played by different actors within the system. It involves describing the interactions between actors and the system as a sequence of messages.

Use case diagrams are used to visually represent these interactions and the different use cases that the system supports. These diagrams illustrate the relationships between actors and use cases, as well as the flow of interactions between them. By using use case diagrams, we can identify the various functionalities or services that the system needs to provide and determine the actors who will interact with it.

#### Activity view - Activity diagram
The activity view focuses on the flow of control or object flow among the steps of a computation or workflow. It represents computational activities involved in performing calculations or workflows. 

Activity diagrams can be seen as an advanced version of a flow chart, as they model the flow from one activity to another. The actions coordinated by activity models can be initiated when other actions finish executing, when objects and data become available, or when certain external events occur. Activity diagrams are particularly useful for visualizing workflows, business processes, or the logic of complex algorithms.

#### State machine view - State machine diagram/State Transition Diagram.
The state machine view is used to depict the potential life cycles of an object belonging to a class. It consists of states connected by transitions, where each state represents a specific period in the object's life, characterized by certain conditions being met.

State machine diagram are behavioral diagrams that illustrate the various states an object or system can assume and how it transitions between those states based on events or conditions. These diagrams are particularly useful when modeling systems in which behavior is dependent on the current state, such as user interfaces or control systems.

#### Interaction view - Sequence diagram
The interaction view describes sequences of message exchanges among the parts of a system. One use of sequence diagrams is to show the behavioral sequence of a use case. They illustrate the sequence of interactions between objects over time. 

Sequence diagrams are useful for designing and documenting interactions between different components or objects in the system, especially in scenarios where the timing and order of messages are important. They concentrate on modeling the interactions between objects or components within a system, showcasing the sequence of messages exchanged between objects and highlighting their order and timing. Sequence diagrams provide a detailed view of the interactions and collaborations between objects, including the exchange of messages, method invocations, and responses.

#### Deployment view - Depolyment diagram
A deployment view shows the deployment of runtime artifacts on nodes. Nodes represent runtime resources such as computers or memory, while artifacts are physical implementation units such as files. This view allows the consequences of distribution and resource allocation to be assessed. 

Deployment diagrams are used to model the physical aspects of an object-oriented system. They depict the static deployment view of a system, showing the topology of the hardware and how runtime artifacts are deployed on the nodes.

#### Model management view - Package diagram   
Model management consists of packages and dependency relationships among them, which allow a large system to be divided into smaller units. The model management view models the organization of the model itself and comprises a set of packages that hold model elements such as classes, state machines, and use cases. 

Package diagram demonstrates the arrangement and organization of model elements in a medium to large-scale project. Package diagrams can represent both the structure and dependencies between subsystems or modules, providing different views of a system, such as a multi-layered application model in a multi-tiered application architecture.

<br>

---

#### References

Fakhroutdinov, K.  The Unified Modeling Language.  Available from: https://www.uml-diagrams.org/ [Accessed 8 April 2024]

IBM Documentation. (2023) UML models and diagrams.  Available from: https://www.ibm.com/docs/en/rational-soft-arch/9.7.0?topic=diagrams-uml-models [Access 15 April 2024] 

Rumbaugh, J., Jacobson, I. & Booch, G. (2004) The Unified Modeling Language Reference Manual. 2nd ed. Boston: Addison-Wesley.  

Visual Paradigm. Overview of the 14 UML Diagram Types.  Available from: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/overview-of-the-14-uml-diagram-types/ [Accessed 15 April 2024]


---

[Return to Module 2 Unit 3](OOP_Unit03.md)
