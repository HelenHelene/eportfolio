# Vulnerability Analysis – Literature Review Activity

### Instructions
Based on the information identified about your assigned websites, carry out a literature search/ audit on [Gin & Juice Shop Ecommerce](https://ginandjuice.shop/) and the national vulnerabilities database to create a baseline audit on potential vulnerabilities with websites.

This article combines a baseline audit on potential vulnerabilities and an asset analysis for the [Gin & Juice Shop Ecommerce](https://ginandjuice.shop/). It outlines the approach, methodologies, and tools for auditing and assessing security vulnerabilities, ensuring compliance with relevant standards, and improving overall site security

### Learning Outcomes
 - Identify and analyse security threats and vulnerabilities in network systems and determine appropriate methodologies, tools and techniques to manage and/or solve them.
 - Design and critically appraise computer programs and systems to produce solutions that help manage and audit risk and security issues.
 - Gather and synthesise information from multiple sources (including internet security alerts and warning sites) to aid in the systematic analysis of security breaches and issues.

### Asset ID and Analysis Audit
 - Human assets
 - Web assets
 - Physical assets

### Identify Required Scans and Tools

#### Network Scans
If the requirement is to test for network vulnerabilities, then tools such as traceroute, Nmap, and Nessus (amongst many others) should be used.
- **PING** : using Ping will tell you little about an individual website using shared hosting. Instead, it will report on the underlying host which may be shared by several (perhaps dozens) of websites.
- **NMAP** : a tool like Nmap may also give erroneous reports due to the fact that, by default, it will examine the resource indicated by the IP address rather than the URL. As such, Nmap will try and report on ALL the services/ resources running on the host rather than the site or application in question. i.e., give misleading information when used to probe a shared IP web site.

#### Host Scans
When the requirement is to scan/audit the underlying host itself, for example, if working for a hosting company or dealing with on-premise resources, a different set of tools is required.
 - **IDS** : The most common tool deployed when scanning or auditing a host platform is a host-based intrusion detection system (HIDS). Most HIDS operate by creating a hash of key system files or objects (such as the etc/shadow or etc/passwd on Unix systems, or the registry hives such as HKEY_USERS files on Windows). If these files change unexpectedly (for example, without corresponding log entries or equivalent), the HIDS can trigger an alert. Commonly utilised applications for this function include Snort, which can act as both a HIDS and NIDS (network intrusion detection system), and Tripwire. NIDS often use externally managed databases of signatures to detect and track network intrusion attempts (Rubens, 2015). Many commercial anti-virus suites offer similar functionality.
 - **Hardware Audits** : Hardware audits are often carried out by network-based tools. One of the most common is Microsoft Configuration Manager (which used to be called Microsoft SCCM – system centre configuration manager). This can often help if low-level viruses attempt to change BIOS or firmware code, or if third parties have hijacked your server(s) to use as part of their botnet farms.
 - **Log Analysis** : The final aspect of host scanning is log analysis and auditing.

#### Wireless Scans
Wireless scans are often viewed as part of an overall network audit, but they are becoming increasingly important as mobile devices proliferate in the enterprise.
 - **Kismet** : The traditional, most flexible of the wireless scanning and auditing tools is Kismet (Kismet, 2022) which can probe wireless interfaces, 'sniff' network traffic and even act as a WIDS (wireless intrusion detection system). It is also available as part of the Kali Linux distribution (see later).
 - **Aircrack-ng** : A more focused tool is aircrack-ng (and its associated suite) which is designed to capture and extract keys and passphrases from encrypted wireless traffic. A paper by Carranza et al (2018) provides a tutorial for using Kismet, aircrack-ng and associated tools.

### Application Scanning/Management Tools
The final target for scanning and auditing are the applications that are deployed and run on the system(s) under consideration. 
 - **MS CM (SCCM)** : Microsoft configuration manager (discussed previously) provides a number of services that can be used to audit and manage applications, including deployment, the enforcement of group policies, and the management of automated updates.
 - **AppArmor** : On Unix-like systems (particularly Linux), there is a tool called AppArmor which "provides MAC functionality to Linux and is used to supplement the traditional DAC (file permissions) functionality that the OS provides." (Shamim, 2016). Essentially, it provides profiles that can be used to monitor (log) or prevent applications from accessing resources and being utilised by unauthorised users. So AppArmor can be used for both auditing and management of applications.

### Core Software Network Components and Tools
There are a number of tools that over time have become part of the 'Internet Protocol' suite – these include
 - **PING** : PING is one of the oldest utilities that uses the IP stack. Its main purpose is to determine if a specific host is available, and to also calculate the round trip time (RTT) required to send a basic message from a source to a target address and receive a reply.
 - **TRACEROUTE / TRACERT** : Traceroute is a utility that is used to display a route between two hosts, as well as calculating the transit delay caused by the routers traversed during the journey.
 - **NSLOOKUP** : NSlookup (name server lookup) is a utility used to query the DNS (domain name server) system. 
 - **DIG** : DIG (rumoured to be Domain Internet Groper) is a more modern version of nslookup, with more features.
 - **WHOIS** : WHOIS is a Unix utility that is commonly used to query the Internet registrar databases.
 - **NETSTAT** : Netstat (network statistics) is a multiplatform utility used to show the active connections from a system to external hosts.
 - **Internet / Web-based services** : There are a number of third-party, web-based utilities that provide a basic system check for home-based systems – one of the oldest (but still very useful) is found at www.grc.com (then click on ShieldsUp on that page to access the scanning systems).  This will test which ports are open on your system and also how good the security of your internet gateway/router is (for example, how much information does it expose?).
 - **Web Spider** : A final tool type often used by attackers (as well as search engines) is a web spider – this tool will work its way through every page available on your website and index (or download) the HTML to reconstruct it offline.

### Packet Diagnostic and Analysis Tools
 - **TCPDUMP** : TCPDump is a Unix-style, command line tool found on most modern Unix like systems (e.g. BSD, Linux, etc). That means it is usually shipped as standard on most modern xBSD and Linux systems.
 - **WIRESHARK** : Wireshark performs a similar function to TCPDump except it is a GUI based tool, and is available for multiple platforms including Linux, MacOS and Windows. 

### Vulnerability and Port Scanners
 - **NMAP** : Nmap is another command line based scanning tool. It is usually used for service and OS discovery as part of a vulnerability scan. 
 - **NESSUS** : Nessus is a commercial vulnerability scanner, again available for multiple platforms.
 - **OPENVAS** : OpenVAS (the open vulnerability assessment system) is an open-source tool, based on the same core as Nessus. It is a server-based system, available as a downloadable image that runs within a virtual machine – as such it is a form of virtual appliance. It is designed to be controlled by the host machine – which means the VMM needs to be configured to receive network traffic both from the internet and the host machine itself. The main difference between tools like Nmap and Nessus derivatives is the presence of a data feed that contains information about known vulnerabilities and how to detect them.
 - **KALI LINUX** : The final toolset on the list is Kali Linux – short for Kernel Auditing Linux it is a Linux distribution that comes pre-packaged with a large number of testing tools including Wireshark, NMap and many others. It is available as a 'live' distribution (I.e. requires no installation) on DVD or USB and also runs within a VM.

[Risk Mapping for Assignment 1](NS_Unit02_RiskMapping.pdf)

### Reflections
Reflect on this activity by answering the following questions:
 - Did you have any issues or challenges with the literature search/audit on software sites and the national vulnerabilities database?
 - How did you overcome them?
 - How will they affect your final report?

### Reference
Unit 3 Lecturecast - Vulnerability Assessments

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

