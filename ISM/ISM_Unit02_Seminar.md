# Unit 2 Seminar Exercise – Threat Model for a Large International Bank

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

| **STRIDE** | **Threats** |
| :--------- | :-------- |
| Spoofing | Unauthorized access to customer accounts. |
| Tampering | Alteration of transaction data. |
| Repudiation | Denial of fraudulent transactions. |
| Information Disclosure | Leakage of customer financial information. |
| Denial of Service | Disruption of online and mobile banking services. |
| Elevation of Privilege | Gaining higher-level access to internal banking systems. |

### Step 4: Analyze Threats

| **STRIDE** | **ATT&CK** | **Example** |
| :--------- | :-------- | :---------- |
| Spoofing | **T1078.001** Valid Accounts: Default Accounts | An attacker impersonates a bank customer to access their account. |
| Tampering | **T1565.001** Data Manipulation: Stored Data Manipulation | Malware introduced into the transaction processing system to alter transaction amounts. |
| Repudiation | **T1585.001** Establish Accounts: Social Media Accounts | A customer denies having performed a transaction after their account is compromised. |
| Information Disclosure | **T1005** Data from Local System | Unauthorized access to the bank's database leading to leakage of customer data. |
| Denial of Service | **T1499** Endpoint Denial of Service | DDoS attack on the bank’s online banking platform. |
| Elevation of Privilege | **T1068** Exploitation for Privilege Escalation |Exploiting a vulnerability in the bank's internal systems to gain administrative access. |

#### Step 5: Evaluate Threats

| **STRIDE** | **DREAD** | **Rating** |
| :--------- | :-------- | :---------- |
| Spoofing | Damage | 8 |
| | Reproducibility | 6 |
| | Exploitability | 7 |
| | Affected Users | 8 |
| | Discoverability | 4 |
| **DREAD Score** | | **33** |
| Tampering | Damage | 9 |
| | Reproducibility | 5 |
| | Exploitability | 6 |
| | Affected Users | 8 |
| | Discoverability | 5 |
| **DREAD Score** | | **33** |
| Information Disclosure | Damage | 8 |
| | Reproducibility | 7 |
| | Exploitability | 6 |
| | Affected Users | 9 |
| | Discoverability | 5 |
| **DREAD Score** || **35** |

### Step 6: Develop Mitigations
Spoofing: Implement multi-factor authentication for customer account access.
Tampering: Use integrity checks and monitoring on transaction processing systems.
Information Disclosure: Encrypt data at rest and in transit, and implement stringent access controls on databases.

### Step 7: Validate
Review: Regularly review and update the threat model based on new intelligence and changes in the threat landscape.
Test: Conduct penetration testing and red team exercises to validate the effectiveness of mitigations.

### Principles from the Threat Modeling Manifesto
Culture of Finding and Fixing Design Issues: Focus on identifying and resolving design issues rather than mere compliance.
People and Collaboration: Foster collaboration among diverse teams to bring various perspectives to the threat modeling process.
Continuous Refinement: Regularly refine and update the threat model to adapt to new threats and vulnerabilities.

### OWASP Threat Modeling Cookbook
Systematic Approach: Use a structured methodology to ensure thorough and reproducible threat modeling.
Informed Creativity: Combine creative thinking with scientific rigor to identify potential threats.
Varied Viewpoints: Involve subject matter experts from different domains to gain diverse insights.
Useful Toolkit: Utilize tools that enhance productivity, repeatability, and measurability of the threat modeling process.
Theory into Practice: Apply field-tested techniques that are aligned with the latest best practices and local needs.

### ATT&CK Libraries
Leverage the ATT&CK framework to identify potential adversary techniques and tactics that could be used to exploit the system.

### Reflections
This threat model highlights the importance of securing both digital and physical assets of a large international bank. The use of STRIDE and DREAD frameworks provides a structured approach to identifying and evaluating threats. Incorporating principles from the Threat Modeling Manifesto ensures a comprehensive and collaborative approach to threat modeling.

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
