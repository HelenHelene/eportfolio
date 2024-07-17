# Unit 4 Seminar – DR Solutions Design and Review

Activities before Unit 4 seminar.

### Activity 1: DR Terms and Concepts
Read [Alhazmi & Malaiya (2013)](ISM_Unit04_SeminarReading1.pdf) and then answer the following questions:

#### RPO (Recovery Point Objective)
**Definition:** RPO indicates the maximum acceptable amount of data loss measured in time. It determines how much data the organization can afford to lose in case of a disruption.

**Key Points:**
 - **Data Loss Tolerance:** RPO defines the point in time to which data must be recovered after an outage. It answers the question, "How much data can we afford to lose?"
 - **Backup Frequency:** The RPO influences the frequency of backups. A shorter RPO requires more frequent data backups.
 - **Impact on Operations:** A low RPO might necessitate real-time or near-real-time data replication, which can impact operational costs and complexity.

#### RTO (Recovery Time Objective)
Definition: RTO is the maximum acceptable amount of time to restore a system or application after a disaster to avoid significant impacts on business operations.

Key Points:

Downtime Tolerance: RTO defines the time within which the business process must be restored after an outage. It answers the question, "How quickly do we need to recover?"
Impact on Recovery Strategy: The RTO determines the required speed of recovery operations. A shorter RTO requires faster recovery solutions, which might involve more resources and higher costs.
Service Continuity: A low RTO ensures that business operations resume swiftly, minimizing the impact on service continuity.
Comparison:
RPO: Focuses on data loss (how much data can be lost).
RTO: Focuses on downtime (how quickly the system must be back up).
Example:
Consider a financial company that processes transactions every minute:

RPO: If the company sets an RPO of 5 minutes, it means they can afford to lose up to 5 minutes of data in a disaster. Therefore, they need to back up their data at least every 5 minutes.
RTO: If the company sets an RTO of 1 hour, it means they need to restore their systems and resume operations within 1 hour of any disruption to avoid significant impact on their business.

#### 1. What is the difference between Hot Standby, Warm Standby and Cold Standby? Frame your answers in terms of availability, RPO and RTO.

### Hot Standby:
Availability: Highest availability.
RPO: Near-zero or very low, as data is continuously synchronized.
RTO: Near-zero or very low, as the system is ready to take over immediately.
Hot standby refers to a fully operational backup system that receives live updates and can take over instantly in case of a primary system failure. This setup ensures minimal disruption to services.

### Warm Standby:
Availability: Moderate availability.
RPO: Low to moderate, with periodic synchronization.
RTO: Moderate, as the system may require some configuration and data synchronization before it can become fully operational.
Warm standby involves a backup system that is partially configured and receives periodic updates. It requires some time to become fully operational after a failure.

### Cold Standby:
Availability: Lowest availability.
RPO: Highest, with less frequent or no synchronization.
RTO: Highest, as the system needs to be started and configured from scratch.
Cold standby refers to a backup system that is not operational and requires significant time to be brought online and made ready to take over.

2. Does the technology deployed affect the options available? For example, can you create a high availability, hot standby solution between two on-premise data centres?

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
