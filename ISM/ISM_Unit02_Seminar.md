# Unit 2 Seminar Exercise – Threat Model for a Large International Bank

## Threat Modeling Process Summary
1. **Define the Scope:** Identify the system components and boundaries.
2. **Identify Assets:** Determine critical assets that need protection.
3. **Identify Threats:** Use STRIDE to categorize and identify potential threats.
4. **Analyze and Evaluate Threats:** Leverage frameworks like DREAD or ATT&CK to evaluate threats.
5. **Develop Mitigations:** Implement mitigations using guidelines from the OWASP Threat Modeling Cookbook.
6. **Validate:** Regularly review, test, and update the threat model.

## Step 1: Define the Scope
### System Description:
 - Online banking platform
 - Mobile banking applications
 - Internal banking systems
 - ATMs and physical branches
 - Communication networks
 - Data centers and cloud services

## Step 2: Identify Assets
### Critical Assets:
 - Customer data (PII, financial information)
 - Transaction data
 - Online and mobile banking platforms
 - Internal banking systems
 - Network infrastructure
 - Physical security systems (ATMs, branch security)
 - Data centers and cloud services

## Step 3: Identify Threats
Using STRIDE to categorize threats:

| **STRIDE** | **Threats** |
| :--------- | :-------- |
| Spoofing | Unauthorized access to customer accounts. |
| Tampering | Alteration of transaction data. |
| Repudiation | Denial of fraudulent transactions. |
| Information Disclosure | Leakage of customer financial information. |
| Denial of Service | Disruption of online and mobile banking services. |
| Elevation of Privilege | Gaining higher-level access to internal banking systems. |

## Step 4: Analyze and Evaluate Threats
Leverage the ATT&CK libraries to identify potential adversary techniques and tactics that could be used to exploit the system.

| **STRIDE** | **ATT&CK** | **Example** |
| :--------- | :-------- | :---------- |
| Spoofing | **T1078.001** Valid Accounts: Default Accounts | An attacker impersonates a bank customer to access their account. |
| Tampering | **T1565.001** Data Manipulation: Stored Data Manipulation | Malware introduced into the transaction processing system to alter transaction amounts. |
| Repudiation | **T1585.001** Establish Accounts: Social Media Accounts | A customer denies having performed a transaction after their account is compromised. |
| Information Disclosure | **T1005** Data from Local System | Unauthorized access to the bank's database leading to leakage of customer data. |
| Denial of Service | **T1499** Endpoint Denial of Service | DDoS attack on the bank’s online banking platform. |
| Elevation of Privilege | **T1068** Exploitation for Privilege Escalation |Exploiting a vulnerability in the bank's internal systems to gain administrative access. |

Using DREAD to evaluate threats:

| **STRIDE** | **DREAD** | **Rating** |
| :--------- | :-------- | :---------- |
| Spoofing: |
| | Damage | 8 |
| | Reproducibility | 6 |
| | Exploitability | 7 |
| | Affected Users | 8 |
| | Discoverability | 4 |
| **DREAD Score** | | **33** |
| Tampering: |
| | Damage | 9 |
| | Reproducibility | 5 |
| | Exploitability | 6 |
| | Affected Users | 8 |
| | Discoverability | 5 |
| **DREAD Score** | | **33** |
| Repudiation: |
| | Damage | 6 |
| | Reproducibility | 5 |
| | Exploitability | 6 |
| | Affected Users | 7 |
| | Discoverability | 4 |
| **DREAD Score** | | **28** |
| Information Disclosure: | 
| | Damage | 8 |
| | Reproducibility | 7 |
| | Exploitability | 6 |
| | Affected Users | 9 |
| | Discoverability | 5 |
| **DREAD Score** || **35** |
| Denial of Service: |
| | Damage | 7 |
| | Reproducibility | 8 |
| | Exploitability | 5 |
| | Affected Users | 9 |
| | Discoverability | 6 |
| **DREAD Score** || **35** |
| Elevation of Privilege: |
| | Damage | 9 |
| | Reproducibility | 6 |
| | Exploitability | 7 |
| | Affected Users | 8 |
| | Discoverability | 5 |
| **DREAD Score** || **35** |

## Step 5: Develop Mitigations
Based on the OWASP Threat Modeling Cookbook, here are the mitigations for all STRIDE categories:

| **STRIDE** | **OWASP Mitigations** | 
| :--------- | :-------- | 
| Spoofing | Implement multi-factor authentication for customer account access. |
| Tampering | Use integrity checks and monitoring on transaction processing systems. |
| Repudiation	| Implement comprehensive logging and monitoring to ensure actions can be tracked and verified. |
| Information Disclosure | Encrypt data at rest and in transit, and implement stringent access controls on databases. |
| Denial of Service	| Implement rate limiting, load balancing, and DDoS protection mechanisms.
| Elevation of Privilege |	Regularly update and patch systems, and use principle of least privilege for access controls.

### OWASP Threat Modeling Cookbook Guidelines
1. **Systematic Approach:** Use a structured methodology to ensure thorough and reproducible threat modeling.
 - Apply security and privacy knowledge in a structured manner.
 - Achieve thoroughness and reproducibility in threat modeling processes.
2. **Informed Creativity:** Combine creative thinking with scientific rigor to identify potential threats.
 - Allow for creativity by including both craft and science.
 - Use diverse techniques and perspectives to uncover threats.
3. **Varied Viewpoints:** Involve subject matter experts from different domains to gain diverse insights.
 - Assemble a diverse team with appropriate subject matter experts.
 - Encourage cross-functional collaboration to capture a wide range of viewpoints.
4. **Useful Toolkit:** Utilize tools that enhance productivity, repeatability, and measurability of the threat modeling process.
 - Support your approach with tools that increase productivity.
 - Enhance workflows and enable repeatability and measurability.
5. **Theory into Practice:** Apply field-tested techniques that are aligned with the latest best practices and local needs.
 - Use successfully field-tested techniques.
 - Align techniques to local needs and be informed by the latest thinking on the benefits and limits of those techniques.

## Step 6: Validate
 - **Review:** Regularly review and update the threat model based on new intelligence and changes in the threat landscape.
 - **Test:** Conduct penetration testing and red team exercises to validate the effectiveness of mitigations.

### Principles from the Threat Modeling Manifesto
Values and Principles from the Threat Modeling Manifesto:
1. **Values:**
 - **Culture of Finding and Fixing Design Issues:** Focus on identifying and resolving design issues rather than mere compliance.
 - **People and Collaboration:** Foster collaboration among diverse teams to bring various perspectives to the threat modeling process.
 - **Continuous Refinement:** Regularly refine and update the threat model to adapt to new threats and vulnerabilities.

2. **Principles:**
 - **Improve Security and Privacy:** The best use of threat modeling is to improve the security and privacy of a system through early and frequent analysis.
 - **Align with Development Practices:** Threat modeling must align with an organization’s development practices and follow design changes in iterations that are each scoped to manageable portions of the system.
 - **Value to Stakeholders:** The outcomes of threat modeling are meaningful when they are of value to stakeholders.
 - **Dialog and Documentation:** Dialog is key to establishing the common understandings that lead to value, while documents record those understandings and enable measurement.

## Reflections
This threat model highlights the importance of securing both digital and physical assets of a large international bank. The use of STRIDE and DREAD frameworks provides a structured approach to identifying and evaluating threats. Incorporating principles from the Threat Modeling Manifesto ensures a comprehensive and collaborative approach to threat modeling, while the OWASP Threat Modeling Cookbook provides practical mitigation strategies, and the ATT&CK libraries offer detailed adversary tactics and techniques to be aware of.

<br><br>

---

### Reference
Kirtley, N. (2023) DREAD Threat Modeling. Available from: https://threat-modeling.com/dread-threat-modeling/ [Accessed 18 June 2024]

Shostack, A. (2014) Threat modeling : designing for security. 1st ed. Wiley & sons ltd

Shostack, A. et al. (2020) Threat modeling Manifesto. Available from: https://www.threatmodelingmanifesto.org/ [Accessed 17 June 2024].

Spring, J. et al (2021) Time to Change the CVSS? Available from: https://ieeexplore.ieee.org/document/9382369 [Accessed 17 June 2024].

<br><br>

---

[Return to Module 4 Unit 4](ISM_Unit04.md)
