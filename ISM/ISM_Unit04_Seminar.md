# Unit 4 Seminar – DR Solutions Design and Review

Activities before Unit 4 seminar.

## Activity 1: DR Terms and Concepts
Read [Alhazmi & Malaiya (2013)](ISM_Unit04_SeminarReading1.pdf) and then answer the following questions:

### Summary of Recovery Point Objective (RPO) and Recovery Time Objective (RTO)
 - Critical components of disaster recovery plans.
 - Define acceptable data loss and system restoration time.
 - Lower RPO and RTO require advanced and costly solutions.
 - Balance based on business needs and resources.
 - Carefully assess RPO and RTO requirement to design effective and cost-efficient disaster recovery solutions.

| **Key Point** | **Recovery Point Objective (RPO)** | **Recovery Time Objective (RTO)**|
| :--- | :--- | :--- |
| **Definition** |  Maximum acceptable amount of **data loss** measured in time. | Maximum acceptable amount of **time to restore** business operations after a disaster. |
| **Importance** | Determines frequency of data backups or replications. | Minimizes downtime. |
|  | Ensures data loss is within acceptable limits during recovery. | Ensures business continuity. |
| **Implementation** | Frequent data backups. | Robust disaster recovery solutions. |
|  | Continuous data replication. | Hot standby systems. |
|  | Technologies like synchronous replication for near-zero RPO. | Automated failover mechanisms. |
|  | | Pre-configured recovery environments. |
| **Complementary Metrics** | Addresses data loss tolerance. | Addresses downtime tolerance. |


#### 1. What is the difference between Hot Standby, Warm Standby and Cold Standby? Frame your answers in terms of availability, RPO and RTO.

| **Mode** | **Availability** | **Cost** | **Recovery Point Objective (RPO)** | **Recovery Time Objective (RTO)**|
| :--- | :--- | :--- | :--- |
| **Hot Standby** | Very high, as the backup site is always running and ready to take over immediately. | Most expensive | Quickest failover with low RPO usually close to zero, as data is continuously synchronized. | Minimal, often a few seconds to minutes, since the system is always on standby. |
| **Warm Standby** | Moderate, as the backup system is partially ready and might require some initialization. | Moderate | Typically a few minutes to hours, depending on the synchronization frequency. | Moderate, ranging from minutes to hours, as some setup and data synchronization might be needed to bring the system online. |
| **Cold Standby** | Low, as the backup site is not operational until needed. | Least expensive | Up to 24 hours or more, as data synchronization might occur less frequently. | Long, potentially taking several hours to days, since the system needs to be powered on, initialized, and synchronized. |

#### 2. Does the technology deployed affect the options available? For example, can you create a high availability, hot standby solution between two on-premise data centres?

Justify and support your answers with appropriate references from academic journals and sources. Add you answers to your e-portfolio and be prepared to share them in this week’s seminar.

### Activity 2: DR Solutions Design
Read Opara-Martins et al (2014) and Morrow et al (2021) and answer the following questions:
1. What are some of the main vendor lock-in issues the authors identify? How would you mitigate them?
2. What are some of the security concerns with the modern cloud? How can these be mitigated?

### Activity 3: DR Solutions Design and Review
Create a high-level diagram of a DR solution for each of the following requirements. They should be created in PowerPoint, and you should include a basic description of each design.
1. RPO= 1 hr; RTO= 8 hrs; high availability (HA) required.
2. RPO= 24 hrs; RTO = 72 hrs; HA NOT required.
3. RPO= 5 mins; RTO= 1 hr; HA required.
   
Add your answers to your e-portfolio and be prepared to discuss them during the seminar this week.

### Learning Outcomes
Identify and analyse security risks, threats and vulnerabilities in information systems and determine appropriate methodologies, tools, and techniques to manage and/or solve them.
Gather and synthesise information from multiple sources (including internet security alerts & warning sites) to aid in the systematic analysis of security breaches & issues.
Critically appraise and utilise methodologies, tools and techniques that help manage and audit security issues

### Reflections
xxx 
<br><br>

---

### Reference
Alhazmi, O. & Malaiya, Y. (2013) Evaluating disaster recovery plans using the cloud. Available from: https://ieeexplore.ieee.org/document/6517700 [Accessed xxx].

Morrow, T. et al. (2021) Cloud Security Best Practices Derived from Mission Thread Analysis. Available from: https://apps.dtic.mil/sti/pdfs/AD1139951.pdf [Accessed xxx].

Opara-Martins, J. et al. (2014) Critical Review of Vendor Lock-in and Its Impact on Adoption of Cloud Computing. Available from: https://eprints.bournemouth.ac.uk/22467/1/Critical%20Review%20of%20Vendor%20Lock-in%20and%20Its%20Impact%20on%20Adoption%20of%20Cloud%20Computing.pdf [Accessed xxx].
<br><br>

---

[Return to Module 4 Unit 4](ISM_Unit04.md)
