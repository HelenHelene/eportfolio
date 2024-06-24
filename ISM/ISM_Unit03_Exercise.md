# Exercise: Security Standards

### Introduction
This exercise is reviewing the following links/ websites and answer the questions below.

 - [ICO - Guide to the General Data Protection Regulation (GDPR).](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/)
 - [PCI Security Standards.org. - Official PCI Security Standards Council Site - PCI Security Standards Overview.](https://www.pcisecuritystandards.org/standards/)
 - [HIPAA. - HIPAA For Dummies – HIPAA Guide.](https://www.hipaaguide.net/hipaa-for-dummies)

These standards are essential for protecting personal data, payment information, and health information. They provide guidelines for organizations to implement strong security measures and maintain compliance to protect sensitive information. Below are the key aspects of each standard:

### General Data Protection Regulation (GDPR)
The GDPR is a comprehensive data protection law implemented by the European Union (EU) that has been in effect since May 25, 2018. GDPR is designed to protect the personal data and privacy of individuals within the EU and the European Economic Area (EEA). It also regulates the transfer of personal data outside these regions.

Key aspects of GDPR include:
 - **Data Protection Principles:** Ensuring personal data is processed legally, fairly, and transparently.
 - **Data Subject Rights:** Giving individuals rights such as access to their data, the right to correct or delete it, and the right to data portability.
 - **Accountability and Governance:** Requiring organizations to show they comply with GDPR through proper documentation and assessments.
 - **Penalties:** Imposing high fines for non-compliance, up to €20 million or 4% of the global annual turnover, whichever is higher.
   
### Payment Card Industry Data Security Standard (PCI DSS)
The PCI DSS is a set of security standards to ensure that all companies that accept, process, store, or transmit credit card information maintain a secure environment. These standards were developed by the Payment Card Industry Security Standards Council (PCI SSC).

Key components of PCI DSS include:
 - **Build and Maintain a Secure Network:** Installing and maintaining firewalls to protect cardholder data.
 - **Protect Cardholder Data:** Encrypting cardholder data during transmission over public networks.
 - **Maintain a Vulnerability Management Program:** Using and regularly updating antivirus software and developing secure systems.
 - **Implement Strong Access Control Measures:** Limiting access to cardholder data based on business needs and assigning unique IDs to each person with computer access.
 - **Monitor and Test Networks:** Regularly checking networks to ensure security measures are effective.
 - **Maintain an Information Security Policy:** Developing a security policy for employees and contractors.

### Health Insurance Portability and Accountability Act (HIPAA)

The HIPAA is a U.S. law enacted in 1996 that provides data privacy and security for safeguarding medical information. It aims to protect sensitive patient health information from being disclosed without the patient's consent or knowledge.

Key rules under HIPAA include:
 - **Privacy Rule:** Sets national standards for the protection of health information and limits its use and disclosure without patient permission.
 - **Security Rule:** Requires organizations to implement safeguards to ensure the confidentiality, integrity, and availability of electronic health information.
 - **Breach Notification Rule:** Requires notifications to be sent out if there is a breach of unsecured health information.
 - **Enforcement Rule:** Details how investigations and penalties for HIPAA violations are conducted, including civil and criminal penalties.
   
---

#### 1. Which of the standards discussed in the sources above would apply to the organisation discussed in the assessment? For example, a company providing services to anyone living in Europe or a European-based company or public body would most likely be subject to GDPR. A company handling online payments would most likely need to meet PCI-DSS standards.
<br>

Based on the case study and the information from the provided sources, the following standards would apply to Pampered Pets:

| **Standard** | **Justification** |
| :----------- | :---------------- |
| **GDPR** | Since Pampered Pets operates in the UK and handles customers' personal data (e.g., through email orders and digital transaction records), they must comply with GDPR to protect individuals' privacy and data rights. |
| **PCI DSS** | Given that transactions are recorded digitally and likely involve processing payment card data, Pampered Pets must comply with PCI DSS to ensure the security of cardholder data. |

---

#### 2. Evaluate the company against the appropriate standards and decide how would you check if standards were being met?
<br>

### GDPR:

   | **Compliance** | **Detail** | **Checking** |
   | :------------- | :---------------- | :----------- |
   | Data Collection and Processing | Pampered Pets collects personal data through email orders and in-store transactions. They must ensure lawful, fair, and transparent processing of this data. | Review how data is collected, stored, and processed. Ensure that there is a lawful basis for each type of data processing and that data subjects are informed about their rights. |
   | Data Security | Appropriate technical and organizational measures must be in place to secure personal data. | Conduct regular security audits to identify vulnerabilities and ensure encryption and secure storage of personal data. Verify that security measures are up-to-date and effective. |
   | Data Subject Rights | Customers should be informed about their rights regarding their personal data, including access, rectification, and deletion. | Evaluate procedures for handling data subject requests. Ensure that requests are processed within the required timeframes and that customers are informed about their rights through clear privacy notices. |
   | Accountability and Governance | Proper documentation and evidence of compliance with GDPR, including data protection impact assessments (DPIAs) where necessary. | Review documentation practices and ensure that records of data processing activities are maintained. Conduct DPIAs for new data processing activities that could pose high risks to data subjects. |

### PCI DSS:

   | **Compliance** | **Detail** | **Checking** |
   | :------------- | :---------------- | :----------- |
   | Secure Network | Implement and maintain a secure network through firewalls and secure configurations of network devices. | Conduct network vulnerability scans and penetration tests to ensure firewalls and security configurations are effective. Regularly update and patch network devices. |
   | Protect Cardholder Data | Encrypt transmission of cardholder data across open, public networks. | Verify that all payment data is encrypted during transmission. Conduct periodic reviews of encryption methods to ensure they meet current standards. |  
   | Access Control | Implement strong access control measures to restrict access to cardholder data. | Review access control policies and ensure that only authorized personnel have access to payment data. Implement two-factor authentication where possible. |
   | Monitoring and Testing | Regularly monitor and test networks to ensure security measures are effective. | Set up continuous monitoring systems to detect and respond to security threats. Perform regular audits and security assessments. |
   | Information Security Policy | Maintain a robust information security policy. | Review and update the information security policy regularly. Ensure all employees are aware of and trained on the policy. |

---
   
#### 3. What would your recommendations be to meet those standards?
<br>

### GDPR Compliance:

   | **Recommendation** | **Detail** |
   | :------------------ | :--------- |
   | Conduct a Data Audit | Identify what personal data is being collected, how it is processed, and ensure lawful bases for processing. |
   | Create Privacy Policies | Develop clear privacy policies and notices to inform customers about their data rights and how their data is used.
   | Implement Data Protection Measures | Use encryption, secure passwords, and regular updates to protect personal data. Ensure that employees are trained on data protection principles.
   | Document Compliance | Maintain records of data processing activities and ensure that consent is obtained where necessary. Perform DPIAs for new data processing activities that could pose high risks to data subjects.

### PCI DSS Compliance:

   | **Recommendation** | **Detail** |
   | :------------------ | :--------- |
   | Secure the Wireless Network | Ensure that the wireless network used by the staff is secure and separate from the network used for transactions. |
   | Encrypt Payment Data | Use encryption methods for storing and transmitting cardholder data. |
   | Access Controls | Implement strong access controls to ensure only authorized personnel have access to payment data. Use two-factor authentication where possible. |
   | Regular Security Testing | Conduct regular vulnerability assessments and penetration tests to identify and fix security weaknesses. |
   | Employee Training | Train staff on PCI DSS requirements and safe handling of cardholder data. |

---
   
#### 4. What assumptions have you made?
<br>

   | **Assumption** | **Detail** | 
   | :------------- | :---------------- | 
   | Personal Data Handling | It is assumed that Pampered Pets handles personal data of customers through email communications and digital transactions. |
   | Payment Processing | It is assumed that payment cards are used for transactions, necessitating PCI DSS compliance. |
   | Limited Digital Infrastructure | Given the small size of the business and the use of an old networked computer, it is assumed that the current IT infrastructure is limited and may require significant upgrades to meet compliance standards. |
   | Customer Base | It is assumed that the customer base is primarily local, but the business has the potential to expand its reach both online and internationally. |
   | Resource Availability | It is assumed that with the funding from Orla O’dour, the business has the financial resources to invest in necessary compliance measures and digital transformation. |

---

### Reflections
This exercise involved evaluating security standards—GDPR, PCI DSS, and HIPAA—and their application to Pampered Pets, the company discussed in Assignment 1. It provided insights into managing information security risks and the importance of these standards for protecting sensitive data.

Throughout the reading of the assigned websites, I learned that GDPR focuses on personal data handling, PCI DSS on payment data security, and HIPAA on medical information protection. Gathering information from sources like the ICO, PCI Security Standards Council, and HIPAA Guide helped in understanding each standard's requirements. This is the basis for analyzing potential security breaches.

For Pampered Pets:
 - **GDPR:** Ensuring lawful data processing and customer rights.
 - **PCI DSS:** Securing networks and encrypting payment data.
 - **HIPAA:** Does not apply to Pampered Pets.

This exercise underscored the ongoing nature of compliance and the critical role of security standards in protecting sensitive information and maintaining trust, which will be the foundation of the upcoming assignment.
<br><br>

---

### Reference
GDPR. (n.d.) General Data Protection Regulation. Available from: https://gdpr.eu/tag/gdpr/ [Accessed 22 June 2024].

ICO. (n.d.) UK GDPR guidance and resources. Available from: https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/ [Accessed 22 June 2024].

PCI Security Standards Council. (n.d.) PCI Security Standards Overview. Available from: https://www.pcisecuritystandards.org/standards/ [Accessed 22 June 2024]

HIPAA. (n.d.) HIPAA For Dummies – HIPAA Guide. Available from: https://www.hipaaguide.net/hipaa-for-dummies [Accessed 23 June 2024].
<br><br>

---

[Return to Module 4 Unit 3](ISM_Unit03.md)
