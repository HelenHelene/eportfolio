### Assignment 1: A Design Proposal of Software to Support Operation of a Driverless Car

<br>

#### Introduction
This report presents a design proposal for the development of software that supports the operation of a driverless car and demonstrated using Unified Modeling Language (UML).

#### Background Research
Prior to commencing the design process, extensive background research was conducted on terms such as autonomous vehicles, driverless cars, robotic cars, self-driving cars, lane decision/lane-keep assist (LKA), emergency brake/automatic emergency braking (AEB), and obstacle/object detection. The purpose of this research was to identify key concepts and common features that contribute to the operation of driverless cars, with a particular emphasis on safety-related capabilities.

#### Definition of a Driverless Car
According to Reddy (2019), a driverless car, also known as a self-driving car, robot car, or autonomous car, is a vehicle that possesses the ability to perceive its surroundings and operate with minimal or no intervention from a human driver.

#### Selected Operations
This proposal focuses on designing a driverless car at Level 3 - Conditional Driving Automation to Level 4 - High Driving Automation, capable of handling most normal driving conditions and monitoring its surroundings (SAE International 2021). 
Three key operations have been chosen as the foundation for safety:

1.	**Lane Detection:** This operation utilizes computer vision algorithms to analyze lane position and orientation, ensuring that the driverless car stays within its designated lane (Fathy et al., 2020).
2.	**Obstacle Detection:** This operation determines when an object poses a dangerous obstacle based on precise distance and position information between the vehicle and the obstacle, provided by sensor technologies (Sosa & Velazquez, 2007). 
3.	**Emergency Brake:** This feature adds an additional layer of safety to obstacle detection by automatically applying the brakes in critical situations to prevent accidents.

#### Proposed Functionality
The proposed driverless car will autonomously drive along a designated path at a maximum speed of 50 km/h or below. Users can start the engine, stop the car by applying the brakes, and turn off the engine to exit the operation. Once the engine is started, the car will move forward while continuously detecting the lane and obstacles. In the event of a lane deviation, it will automatically correct its course towards the center. When an obstacle is detected during motion, the car will first reduce its speed and then apply the brakes once it reaches the minimum safe distance to the obstacle. If no lane deviation or obstacle is detected and the maximum speed is reached, the driverless car will maintain its speed until an obstacle is detected or the user applies the brakes to stop the car. All action history will be collected at the backend, and users can access the history through a frontend interface.

#### UML Models
To represent the design and operation of the driverless car system, the following UML models are utilized:

<img src="OOP_Assignment1_UseCase.jpg?raw=true"> 
<br>
<img src="OOP_Assignment1_Class.jpg?raw=true">
<br>
<img src="OOP_Assignment1_Activity.jpg?raw=true">
<br>
<img src="OOP_Assignment1_Sequence.jpg?raw=true">
<br>
<img src="OOP_Assignment1_StateMach.jpg?raw=true">
<br>

#### Conclusion: 
This design proposal outlines the capabilities and structure of the software that supports the operation of a driverless car.  take into account potential future growth, changes and expansion, the software is designed throught the use of object-oriented program(OOP). The incorporation of UML models facilitates the design and implementation process. By incorporating key features and functionalities, the software aims to ensure safe and efficient autonomous driving.

<br><br>

---

#### References
Fathy, M. et al. (2020) Design and implement of self-driving car.  Procedia Computer Science 175(2020): 165-172. DOI: https://doi.org/10.1016/j.procs.2020.07.026

IBM Documentation. (2023) UML models and diagrams. Available from: https://www.ibm.com/docs/en/rational-soft-arch/9.7.0?topic=diagrams-uml-models [Access 15 April 2024]

Kanchana, B. et al. (2021) Computer Vision for Autonomous Driving.  2021 3rd International Conference on Advancements in Computing 2021: 175 – 180. DOI: https://doi.org/10.1109/ICAC54203.2021.9671099

Reddy, P. P. (2019) Driverless Car: Software Modelling and Design using Python and Tensorflow.  Available from: https://easychair.org/publications/preprint/k7wj [Accessed 14 April 2024].

Rumbaugh, J., Jacobson, I. & Booch, G. (2004) The Unified Modeling Language Reference Manual. 2nd ed. Boston: Addison-Wesley.

SAE International (2021).  Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles J3016_202104.  Available from: https://www.sae.org/standards/content/j3016_202104/ [Accessed 23 April 2024].

Sosa, R. & Velazquez, G. (2007) Obstacles detection and collision avoidance system developed with virtual models. 2007 IEEE International Conference on Vehicular Electronics and Safety 2007: 1-8.  DOI: https://doi.org/10.1109/ICVES.2007.4456397

United States Environmental Protection Agency. (2023) Self-driving Vehicles.  Available from: https://www.epa.gov/greenvehicles/self-driving-vehicles [Accessed 23 April 2024].

Visual Paradigm. Overview of the 14 UML Diagram Types. Available from: https://www.visual-paradigm.com/guide/uml-unified-modeling-language/overview-of-the-14-uml-diagram-types/ [Accessed 15 April 2024]

Zhou, Z. Q. & Sun, L. (2019) Metamorphic testing of driverless cars. Commun. ACM 62(3): 61–67. DOI: https://doi.org/10.1145/3241979

<br><br>

---

[Return to Module 2](OOP.md)
