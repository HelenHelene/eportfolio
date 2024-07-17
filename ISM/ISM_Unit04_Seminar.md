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

 - **Hot standby** refers to a fully operational backup system that receives live updates and can take over instantly in case of a primary system failure. This setup ensures minimal disruption to services.
 - **Warm standby** involves a backup system that is partially configured and receives periodic updates. It requires some time to become fully operational after a failure.
 - **Cold standby** refers to a backup system that is not operational and requires significant time to be brought online and made ready to take over.

| **Mode** | **Availability** | **Cost** | **Recovery Point Objective (RPO)** | **Recovery Time Objective (RTO)**|
| :--- | :--- | :--- | :--- | :--- |
| **Hot Standby** | Very high, as the backup site is always running and ready to take over immediately. | Most expensive | Near-zero or very low, as data is continuously synchronized. | Minimal, often a few seconds to minutes, since the system is always on standby. |
| **Warm Standby** | Moderate, as the backup system is partially ready and might require some initialization. | Moderate | Typically a few minutes to hours, depending on the synchronization frequency. | Moderate, ranging from minutes to hours, as some setup and data synchronization might be needed to bring the system online. |
| **Cold Standby** | Low, as the backup site is not operational until needed. | Least expensive | Up to 24 hours or more, as data synchronization might occur less frequently. | Long, potentially taking several hours to days, since the system needs to be powered on, initialized, and synchronized. |

#### 2. Does the technology deployed affect the options available? For example, can you create a high availability, hot standby solution between two on-premise data centres?

Yes, the technology deployed significantly affects the options available for DR solutions. High availability and hot standby solutions between two on-premise data centres are feasible but require robust infrastructure and technologies such as:
 - **Real-time data replication:** Technologies like synchronous replication ensure that data is identical in both data centres.
 - **Load balancers:** These distribute traffic between the primary and backup systems to ensure seamless failover.
 - **Network infrastructure:** High-speed, reliable network connections between the data centres are essential for real-time data synchronization.
   
While these technologies can enable high availability and hot standby solutions, they also involve higher costs and complexity compared to warm or cold standby setups.

---

### Activity 2: DR Solutions Design
Read [Opara-Martins et al (2014)](ISM_Unit04_SeminarReading2.pdf) and [Morrow et al (2021)](ISM_Unit04_SeminarReading3.pdf) and answer the following questions:

#### 1. What are some of the main vendor lock-in issues the authors identify? How would you mitigate them?

### Main Vendor Lock-In Issues:
1. **Proprietary Technologies and APIs:** Vendors often use proprietary technologies that are not compatible with other systems.
2. **Data Portability:** Difficulty in transferring data from one vendor to another due to proprietary data formats.
3. **High Switching Costs:** Substantial costs associated with migrating applications and data to another provider.
4. **Contractual Lock-In:** Long-term contracts that make it financially challenging to switch vendors.

### Mitigations:
1. **Use of Open Standards:** Favor vendors that support open standards and APIs to ensure compatibility and ease of migration.
2. **Data Portability Tools:** Implement tools and practices that facilitate data export in standardized formats.
3. **Hybrid or Multi-Cloud Strategies:** Distribute workloads across multiple cloud providers to avoid dependency on a single vendor.
4. **Negotiating Flexible Contracts:** Ensure contracts include exit clauses and provisions for data migration.

#### 2. What are some of the security concerns with the modern cloud? How can these be mitigated?

### Security Concerns:
1. **Data Breaches:** Unauthorized access to sensitive data stored in the cloud.
2. **Insufficient Identity and Access Management:** Weak user authentication and access controls.
3. **Insecure APIs:** Vulnerabilities in APIs that can be exploited by attackers.
4. **Misconfiguration:** Improper configuration of cloud resources leading to security gaps.

### Mitigations:
1. **Encryption:** Use robust encryption for data at rest and in transit to protect against unauthorized access.
2. **Multi-Factor Authentication (MFA):** Implement MFA to strengthen identity and access management.
3. **Secure API Practices:** Regularly audit and secure APIs to protect against exploitation.
4. **Regular Audits and Monitoring:** Continuously monitor and audit cloud configurations to identify and rectify misconfigurations.

---

### Activity 3: DR Solutions Design and Review
Create a high-level diagram of a DR solution for each of the following requirements. They should be created in PowerPoint, and you should include a basic description of each design.

1. RPO= 1 hr; RTO= 8 hrs; high availability (HA) required.
2. RPO= 24 hrs; RTO = 72 hrs; HA NOT required.
3. RPO= 5 mins; RTO= 1 hr; HA required.

![DR Solution 1][]Description:- Primary Data Center: Active with real-time data replication.- Secondary Data Center: Passive hot standby, ready to take over within minutes.- Data Replication: Continuous replication to ensure RPO of 1 hour.- Failover Mechanism: Automated failover process to switch operations within 8 hours.2. RPO= 24 hrs; RTO = 72 hrs; HA NOT Required![DR Solution 2][]Description:- Primary Data Center: Active with daily backups.- Secondary Data Center: Cold standby, powered off until needed.- Data Backup: Daily backups to ensure RPO of 24 hours.- Failover Mechanism: Manual failover process with an RTO of up to 72 hours.3. RPO= 5 mins; RTO= 1 hr; HA Required![DR Solution 3][]Description:- Primary Data Center: Active with real-time data replication.- Secondary Data Center: Hot standby, running in parallel.- Data Replication: Near real-time replication to ensure RPO of 5 minutes.- Failover Mechanism: Automated failover with a target of 1 hour.Add these diagrams and descriptions to your e-portfolio and be prepared to discuss them during the seminar this week.


### Reflections
xxx 
<br><br>

---

### Reference
Alhazmi, O. & Malaiya, Y. (2013) Evaluating disaster recovery plans using the cloud. Available from: https://ieeexplore.ieee.org/document/6517700.

Morrow, T. et al. (2021) Cloud Security Best Practices Derived from Mission Thread Analysis. Available from: https://apps.dtic.mil/sti/pdfs/AD1139951.pdf.

Opara-Martins, J. et al. (2014) Critical Review of Vendor Lock-in and Its Impact on Adoption of Cloud Computing. Available from: https://eprints.bournemouth.ac.uk/22467/1/Critical%20Review%20of%20Vendor%20Lock-in%20and%20Its%20Impact%20on%20Adoption%20of%20Cloud%20Computing.pdf.

<br><br>

---

[Return to Module 4 Unit 4](ISM_Unit04.md)
