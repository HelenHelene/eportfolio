# Vulnerability Analysis – Literature Review Activity

### Introduction
This activity conducts the literature review as preparation for the assignment "Vulnerability Audit and Assessment - Baseline Analysis and Plan" on [Gin & Juice Shop Ecommerce](https://ginandjuice.shop/).

### Identified Vulnerabilities
Based on a literature search, the following potential vulnerabilities were identified for the Gin & Juice Shop website:<br>
*Sources: OWASP Top 10, CWE List.*<br>
1. **Broken Access Control (CWE-200, CWE-284)**:
   - Unauthorized access and information disclosure.
2. **Cryptographic Failures (CWE-259, CWE-327, CWE-331)**:
   - Exposure of sensitive information.
3. **Injection (CWE-73, CWE-79, CWE-89)**:
   - Execution of malicious commands or scripts.
4. **Insecure Design (CWE-209, CWE-256, CWE-501, CWE-522)**:
   - Poor security control design leading to vulnerabilities.
5. **Security Misconfiguration (CWE-16, CWE-611)**:
   - Improper security settings causing information exposure.
6. **Vulnerable and Outdated Components (CWE-1104)**:
   - Exploitation of known vulnerabilities in third-party components.
7. **Identification and Authentication Failures (CWE-287, CWE-297, CWE-384)**:
   - Unauthorized access.
8. **Software and Data Integrity Failures (CWE-494, CWE-502, CWE-829)**:
   - Attacks on software updates, data integrity, and insecure deserialization.
9. **Security Logging and Monitoring Failures (CWE-117, CWE-223, CWE-532, CWE-778)**:
   - Delayed incident detection.
10. **Cross-Site Request Forgery (CSRF) and Server-Side Request Forgery (SSRF) (CWE-352, CWE-918)**:
    - Unauthorized actions on authenticated users and unauthorized access to other systems.
11. **Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks (CWE-400, CWE-770)**:
    - Overwhelming server resources.

### Asset ID and Analysis Audit
#### Human Assets
- Website administrators
- Security personnel
- Developers
- Customer support staff

#### Web Assets
- Website front-end (HTML, CSS, JavaScript)
- Backend systems (APIs, database)
- User data and credentials
- Content management system (CMS)

#### Physical Assets
- Servers hosting the website
- Network infrastructure (routers, switches)
- Backup storage devices

### Identify Required Scans and Tools
#### Network Scans
To test for network vulnerabilities, the following tools should be used:
- **Traceroute**: To map the route packets take from the source to the destination.
- **Nmap**: To discover services and open ports on the network.
- **Nessus**: For comprehensive vulnerability scanning.
  
**Considerations**:
- **PING**: Useful for determining the availability of a host, but limited in shared hosting environments.
- **NMAP**: May provide misleading information for shared hosting IP addresses as it scans all services running on the host.

#### Host Scan
For auditing the underlying host:
- **HIDS (Host-based Intrusion Detection System)**: Tools like Snort and Tripwire to monitor key system files for unauthorized changes.
- **Microsoft Configuration Manager (SCCM)**: For hardware audits and detecting unauthorized changes to BIOS or firmware.
- **Log Analysis**: Regular review of system and application logs.

#### Wireless Scans
Important for environments with mobile devices:
- **Kismet**: For wireless network scanning, sniffing, and acting as a wireless intrusion detection system.
- **Aircrack-ng**: For capturing and extracting keys and passphrases from encrypted wireless traffic.

#### Application Scanning/Management Tools
To manage and audit applications on the system:
- **Microsoft Configuration Manager (SCCM)**: For deploying and managing applications and group policies.
- **AppArmor**: On Unix-like systems to monitor and restrict application access.

### Core Software Network Components and Tools
- **PING**: To check host availability and round trip time.
- **Traceroute/Tracert**: To display the route between two hosts and calculate transit delays.
- **NSlookup**: To query DNS records.
- **DIG**: An advanced DNS query tool.
- **WHOIS**: To query Internet registrar databases.
- **Netstat**: To display active connections.
- **Internet/Web-based Services**: Use tools like ShieldsUp from GRC to test open ports and security of internet gateways/routers.
- **Web Spider**: To crawl through website pages and index or download HTML.

### Packet Diagnostic and Analysis Tools
- **TCPDump**: A Unix command-line tool for network packet analysis.
- **Wireshark**: A GUI-based tool for packet analysis, available on multiple platforms.

### Vulnerability and Port Scanners
- **Nmap**: For service and OS discovery as part of vulnerability scanning.
- **Nessus**: A commercial vulnerability scanner for multiple platforms.
- **OpenVAS**: An open-source vulnerability assessment system.
- **Kali Linux**: A Linux distribution with pre-packaged testing tools including Wireshark and Nmap.

### Integration with GRC Website Information
The Gibson Research Corporation (GRC) website offers several tools and resources that can aid in the security audit and vulnerability assessment of the Gin & Juice Shop website. Notable tools include:
- **ShieldsUP!**: To test for open ports and assess the security of internet gateways.
- **DNS Spoofability Test**: To check for DNS-related vulnerabilities.
- **Perfect Passwords**: To generate strong passwords for securing accounts.
- **Leaktest**: To check for potential data leaks.
- **Securable**: To assess the security capabilities of the system.

### Reflection on the Activity
#### Issues or Challenges with Literature Search/Audit
1. **Volume of Data**:
   - **Challenge**: The vast amount of data and reports on vulnerabilities made it challenging to filter relevant information specific to the Gin & Juice Shop website.
   - **Solution**: I focused on the vulnerabilities highlighted by OWASP Top 10 and CWE lists, which are commonly referenced for web applications.
2. **Relevance of Information**:
   - **Challenge**: Ensuring the information was up-to-date and relevant to the specific technologies used by the Gin & Juice Shop website.
   - **Solution**: Cross-referencing multiple sources, including the latest OWASP and CWE updates, helped validate the relevance of the information.
3. **Technical Jargon**:
   - **Challenge**: Understanding and interpreting technical terminologies and vulnerability details.
   - **Solution**: Utilizing glossaries from OWASP and CWE, and seeking clarification from additional reputable sources.

#### How Challenges Were Overcome
- **Focused Search Criteria**: Narrowing down search criteria to focus on web application security and prioritizing well-known vulnerabilities.
- **Utilizing Reliable Sources**: Relying on reputable sources like OWASP, CWE, and NVD to ensure the accuracy and reliability of the information.
- **Continuous Learning**: Leveraging online resources and communities to better understand complex terminologies and concepts.

#### Impact on Final Report
- **Comprehensive Risk Assessment**: The challenges and the solutions implemented ensured a thorough and comprehensive risk assessment.
- **Accurate Recommendations**: The detailed understanding of vulnerabilities will lead to more accurate and actionable recommendations in the final report.
- **Enhanced Security Posture**: Addressing identified vulnerabilities will significantly enhance the security posture of the Gin & Juice Shop website.

---

### Reference
**Unit 3 Lecturecast - Vulnerability Assessments**

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

---

[Return to Module 3 Unit 2](NS_Unit02.md)

