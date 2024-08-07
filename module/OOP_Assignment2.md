### [Assignment 2: System Implementation – README](https://helenhelene.github.io/eportfolio/pdf/Module02_README.pdf)

<br>

🔗[Driverless Car System - Python Scripts](OOP_Assignment2_Scripts.md)

<br>

#### Description
This project implements software to support the operation of a driverless car using OOP principles in Python. It supports three key operations, allowing user interaction through a frontend interface, while the backend simulates data generation and collection. Other required functions like sensors, cameras, and control panels, are assumed to be imported from other subsystems. The corresponding UML diagrams modified in response to feedback, are presented in the **Appendix** for reference.

#### Key Operations
 - **Lane Detection:** Continuously monitors and corrects the car’s position within the lane.
 - **Obstacle Detection:** Detects obstacles in the path and takes appropriate actions.
 - **Emergency Brake:** Activates emergency braking when a critical obstacle is detected.

#### Module and Class Overview
To better organize the code, classes and functions are defined in separate modules and imported into the main program as needed. 

| **Appendix** | **Module** | **Class** | **Description** |
| :----------- | :--------- | :-------- | :-------------- |
| **1** | vehicle.py	| Vehicle	| Base class for generic vehicle with basic functionalities like starting and stopping engine. |
| **2** | driverless_car.py	| DriverlessCar	| Inherits from Vehicle and includes methods for moving, turning, and braking. Integrates lane detection, obstacle detection, and emergency braking. |
| **3** | lane_detection.py	| LaneDetect	| Handles lane deviation detection and correction. |
| **4** | obstacle_detection.py	| ObstacleDetect	| Manages obstacle detection and initiates slowing down or emergency braking. |
| **5** | emergency_brake.py	| EmergencyBrake	| Activates the emergency brake when needed. |
| **6** | backend.py	| Backend	| Collects and stores action history. |
| **7** | frontend.py	| Frontend | Provides text-based interface for interacting with the car and viewing the history. |
| **8** | test.py |  | Contains automated tests to validate the functionality of the driverless car system. |

#### Data Structures Used
 - **List:** Used in the Backend class to store the history of actions. Lists allow efficient appending, suitable for maintaining history log.

#### OOP Features Used
 - **Inheritance:** The DriverlessCar class inherits from the Vehicle class, allowing it to use and extend the functionalities of the base class.
 - **Abstraction:** The system abstracts complex behaviors into simplified interfaces and method calls.
 - **Polymorphism:** Methods like move, turn, and brake in the DriverlessCar class exhibit polymorphic behavior, responding differently based on the context.

#### Execution Instructions
This software is designed to support the operation of a driverless car. It can be executed with additional support from other functions, such as sensors, cameras, and control panels.  The Test Module (test.py) is executed to test the driverless car system and ensure that all components work correctly and interact as expected:
 1.	Ensure Python 3.x is installed on your IDE.
 2.	Ensure all modules are in the same directory.
 3.	Execute the test.py script to perform a series of automated tests validating the system's functionality.
<img src="OOP_Assignment2_Execute.jpg?raw=true">

#### Automated Test Result
The test.py imports all modules and uses Python’s assert statements to achieve automated testing. The tests simulate various actions of the driverless car to ensure all components interact correctly.
 1.	**Start car:** Verifies the engine starts and the speed is initialized to zero.
 2.	**Move car forward:** Ensures the car reaches and maintains the maximum speed.
 3.	**Simulate lane deviation and correction:** Tests the detection and correction of lane deviations.
 4.	**Simulate obstacle detection and slowing down:** Verifies the car slows down when detecting obstacles at a safe distance.
 5.	**Simulate further obstacle detection and emergency brake:** Ensures the car applies the emergency brake if the obstacle is too close.
 6.	**Stop car:** Verifies the car stops and the engine is turned off.
 7.	**View history:** Retrieves and displays the history of all actions taken by the car.

All modules exited normally and below is the expected output of the test: 

<img src="OOP_Assignment2_TestResult.jpg?raw=true">

#### Conclusion
This project demonstrates implementation of software that supports the operation of driverless car using OOP principles. The detailed testing and validation processes ensure that each component performs as intended, contributing to the overall reliability and safety of the system. By modularizing the system into distinct components, the project ensures reusability, maintainability, and scalability.


<br><br>

---

#### Reference
Fathy, M. et al. (2020) Design and implement of self-driving car.  Procedia Computer Science 175(2020): 165-172. DOI: https://doi.org/10.1016/j.procs.2020.07.026

Kanchana, B. et al. (2021) Computer Vision for Autonomous Driving.  2021 3rd International Conference on Advancements in Computing 2021: 175 – 180. DOI: https://doi.org/10.1109/ICAC54203.2021.9671099

Reddy, P. P. (2019) Driverless Car: Software Modelling and Design using Python and Tensorflow.  Available from: https://easychair.org/publications/preprint/k7wj [Accessed 14 April 2024].

Sosa, R. & Velazquez, G. (2007) Obstacles detection and collision avoidance system developed with virtual models. 2007 IEEE International Conference on Vehicular Electronics and Safety 2007: 1-8.  DOI: https://doi.org/10.1109/ICVES.2007.4456397

<br><br>

---

#### Appendix	

<img src="OOP_Assignment2_UseCase.jpg?raw=true">
<br><br>

<img src="OOP_Assignment2_Class.jpg?raw=true">
<br><br>

<img src="OOP_Assignment2_Activity.jpg?raw=true">
<br><br>

<img src="OOP_Assignment2_StateMach.jpg?raw=true">
<br><br>

<img src="OOP_Assignment2_Sequence.jpg?raw=true">
<br><br>

---

[Return to Module 2](OOP.md)
