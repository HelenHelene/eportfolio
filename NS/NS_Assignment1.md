### [Assignment 1: Vulnerability Audit and Assessment - Baseline Analysis and Plan](Module03_BaselineAnalysisAndPlan.pdf)

<br>

#### Introduction
This analysis outlines the approach, methodologies, and tools for auditing and assessing the security vulnerabilities and non-compliance with Web Content Accessibility Guidelines (WCAG), General Data Protection Regulation (GDPR), and Payment Card Industry Data Security Standard (PCI DSS) of Gin & Juice Shop website (G&J) (https://ginandjuice.shop/).

#### Potential Security Challenges and Non-Compliance
Based on Open Worldwide Application Security Project (OWASP) and Common Weakness Enumeration (CWE), the following security risks are relevant to G&J (CWE, 2024; Khan et al, 2019; OWASP Top10, 2021; Priyawati et al., 2022):

| **Risk ID**	| **OWASP**	| **Notable CWEs**	| **Potential Risk** |
| :---------- | :-------- | :--------------- | :----------------- |
| R01 |	Broken Access Control	| CWE-200, CWE-284	| Unauthorized access, information disclosure and modification. |
| R02	| Cryptographic Failures |CWE-259, CWE-327, CWE-331	| Exposure of sensitive information. |
| R03	| Injection 	| CWE-73, CWE-79, CWE-89 | Execution of malicious commands or scripts. |
| R04	| Insecure Design	| CWE-209, CWE-256, CWE-501, CWE-522	| Vulnerabilities resulting from poor security control design. |
| R05	| Security Misconfiguration	| CWE-16, CWE-611	| Improper security settings leading to information exposure. |
| R06	| Vulnerable and Outdated Components	| CWE-1104	| Exploitation of known vulnerabilities in third-party components. |
| R07	| Identification and Authentication Failures	| CWE-287, CWE-297, CWE-384	| Unauthorized access. |
| R08	| Software and Data Integrity Failures	| CWE-494, CWE-502, CWE-829	| Attacks on software updates, data integrity and insecure deserialization. |
| R09	| Security Logging and Monitoring Failures	| CWE-117, CWE-223, CWE-532, CWE-778	| Delayed incident detection. |
| R10	| Cross-Site Request Forgery (CSRF) and Server-Side Request Forgery (SSRF)	| CWE-352, CWE-918	| Unauthorized actions on authenticated users and unauthorized access to other systems. |
| R11	| Denial of Service (DoS) and Distributed Denial of Service (DDoS) attack | CWE-400, CWE-770	| Overwhelming server resources. |

The following standards extracted from WCAG, GDPR, and PCI DSS are applicable to G&J (Krzyminski, 2021; Margau, 2024; Sohaib, 2016):

| **Risk ID**	| **Standard** | **Potential Non-Compliance** |
| :---------- | :----------- | :------------------------- | 
| R12	| WCAG (WCAG, 2023)	| Alternative text for images, captions or transcripts for videos, minimum contrast requirements, keyboard accessibility, duration warning during checkout, and status messages. |
| R13	| GDPR (GDPR, 2024)	| Consent mechanisms, data security measures, documentation of data processing activities, and mechanisms for users to exercise their rights. |
| R14	| PCI DSS (PCI Security Standards Council, 2024)	| Protecting cardholder data, data encryption, and requirements for accepting credit card payments. |

#### Tests and Impacts
To enhance the security of G&J, a combination of automated and manual testing will be conducted remotely. The recommended tools are as follows:

| **Potential Tool** |	**Justification / Explanation** | **Risk ID Mapping** |
| :----------------- | :------------------------------ | :------------------ | 
| Burp Suite (PortSwigger, 2024; OWASP, 2024)	| A powerful web application security tool combining automated scanning and manual testing to assess vulnerabilities, including OWASP Top 10. It's compatible with multiple platforms and has paid and free versions (limited functionality).	| R01 – R08, R10 – R11, R13 – R14 |
| NSlookup (NsLookup, 2023)	| A DNS query tool used to identify DNS vulnerabilities such as misconfigurations and cache poisoning.	| R01, R05, R07 |
| Manual Test	| Accessibility, authentication, payment card data handling, security headers, and PAN masking.	| R01, R07, R09, R12 – R14 | 

Please refer [Appendix I](NS_Unit02_RiskMapping.pdf) for detailed risk mapping.

Negative impacts during testing and recommendations for risk mitigation (Acunetix, 2024):

| **Potential impact** |	**Potential Mitigations** |
| :------------------- | :------------------------ |  
| Damage caused by injected garbage data.	| Run scans on staging environment. |
| Data loss or broken functionality.	| Restrict crawling of sensitive links. |
| Overwhelming web server and causing DoS symptoms.	| Test during off-peak hours. |
| Excessive server logging causing disk space issues.	| Customize scan settings. |

#### Timeline
1.	Proposal Submit: May 20, 2024
2.	Approval of Proposal: May 27, 2024
3.	Vulnerability Audit and Assessment:
    -	Scoping and Planning: 2 working days
    -	Testing and Analysis: 5 working days
    -	Report Compilation: 5 working days
4.	Final Executive Summary Issued: June 10, 2024

#### Limitations and Assumptions
1.	Time limitations impacted the evaluation scope.
2.	The assessment relied on free or trial versions of scanning tools, potentially affecting analysis comprehensiveness.
3.	It assumes disclosed functionality of G&J without considering undisclosed or additional features.

#### Conclusion
The vulnerability audit and assessment of G&J will improve website security, safeguard customer data, and ensure compliance with relevant standards. The executive summary will provide actionable recommendations to mitigate risks and enhance overall website security.

<br><br>

---

#### References
Acunetix. (2024) Negative Impacts of Automated Vulnerability Scanners and How to Prevent them.  Available from: https://www.acunetix.com/support/docs/faqs/negative-impacts-of-automated-vulnerability-scanners-and-how-to-prevent-them/#:~:text=Excessive%20server%20logging,unexpected%20and%20sometimes%20random%20data [Accessed 17 May 2024]

CWE. (2024) CWE List Version 4.14.  Available from: https://cwe.mitre.org/data/index.html [Accessed 16 May 2024].

GDPR. (2024) General Data Protection Regulation.  Available from: https://gdpr.eu/tag/gdpr/ [Accessed 14 May 2024].

Greenbone. (2024) Greenbone OpenVAS.  Available from: https://www.openvas.org/ [Accessed 16 May 2024].

Khan, S. et al. (January 28, 2019) Cyber Security Issues and Challenges in E-Commerce.  Proceedings of 10th International Conference on Digital Strategies for Organizational Success. Available from: https://ssrn.com/abstract=3323741

Krzyminski, A. (June 29, 2021) 94% of the Largest E-Commerce Sites Are Not Accessibility Compliant. Baymard Institute.  Available from: https://baymard.com/blog/accessibility-benchmark-launch [Accessed 14 May 2024].

Margau, A. (January 29, 2024) E-Commerce Web Accessibility: 2024 Essentials & 20 Tips for Businesses.  Clym. Available from: https://clym.io/accessibility-news/e-commerce-web-accessibility-2024-essentials-and-20-tips-for-businesses [Accessed 14 May 2024].

Mudge, M. (2023) 2023 E-Commerce Content Accessibility Report.  Scribely.  Available from: https://www.scribely.com/post/2023-e-commerce-content-accessibility-report [Accessed 14 May 2024].

NsLookup. (2023) How does online nslookup work?.  Available from: https://www.nslookup.io/ [ Accessed 15 May 2024]

OWASP. (2024)  Vulnerability Scanning Tools. Available from: https://owasp.org/www-community/Vulnerability_Scanning_Tools [Accessed 17 May 2024]

OWASP Top10. (2021) OWASP Top 10 - 2021. Available from: https://owasp.org/Top10/ [Accessed 14 May 2024]

PCI Security Standards Council. (2024) PCI Security Standards Overview. Available from: https://www.pcisecuritystandards.org/standards/ [Accessed 15 May 2024]

PortSwigger. (2024) Vulnerabilities detected by Burp Scanner. Available from: https://portswigger.net/burp/documentation/scanner/vulnerabilities-list [Accessed 17 May 2024]

Priyawati, D. et al. (2022) Website Vulnerability Testing and Analysis of Internet Management Information System Using OWASP.  International Journal of Computer and Information System 3(3): 143-147.  DOI: https://doi.org/10.29040/ijcis.v3i3.90

Sohaib, O. & Kang, K. (2016) ‘Assessing Web Content Accessibility of E-Commerce Websites for People with Disabilities’, 25th International Conference on Information Systems Development. Katowice-Poland, August 2016. Poland: ResearchGate.  Available from: https://www.researchgate.net/publication/314210010 [Accessed 14 May 2024].

WCAG. (2023) How to Meet WCAG-Quick Reference.  Available from: https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_overview [Accessed 14 May 2024].
 
<br><br>

---

[Return to Module 3](NS_main.md)
