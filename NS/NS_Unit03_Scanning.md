# Scanning Activity

### Introduction
This activity conducts the basic scan using standard tools such as Traceroute / Tracert and Nslookup as preparation for the Assignment 2 "Vulnerability Audit and Assessment - Results and Executive Summary" on [Gin & Juice Shop Ecommerce](https://ginandjuice.shop/).

### Scanning Output
**Tracert (Windowns) ** <br>
<img src="NS_Unit03_Traceroute.jpg" alt="Traceroute output" width="600"/>

**Nslookup** <br>
<img src="NS_Unit03_Nslookup.jpg" alt="Nslookup output" width="600"/>

### Analysis
1. How many hops from your machine to your assigned website?
   - From the Tracert output, we can see that the command reached 12 hops.
     
2. Which step causes the biggest delay in the route? What is the average duration of that delay?
    - From the Tracert output, we can identify the hop 14 has the highest delay.
    - Average Duration of the Delay:(304 + 304 + 306) / 3 = 304.67 ms
      
3. What are the main nameservers for the website?
    - From the Nslookup output for NS records, below are the main nameservers:
      ns-1543.awsdns-00.co.uk
      ns-1000.awsdns-61.net
      ns-110.awsdns-13.com
      ns-1496.awsdns-59.org
      
4. Who is the registered contact?
   - From the Nslookup output for MX records, the registered contact is : awsdns-hostmaster.amazon.com
 
5. What is the MX record for the website?
 
6. Where is the website hosted?
 - Use https://ipgeolocation.io to identify the physical location of below IP addresses:
   34.249.203.140: Hosted in Ireland (Amazon Web Services)
   34.246.169.176: Hosted in Ireland (Amazon Web Services)
   
### Learning Outcomes
 - Identify and analyse security threats and vulnerabilities in network systems and determine appropriate methodologies, tools and techniques to manage and/or solve them.
 - Design and critically appraise computer programs and systems to produce solutions that help manage and audit risk and security issues.
 - Gather and synthesise information from multiple sources (including internet security alerts and warning sites) to aid in the systematic analysis of security breaches and issues.

### Reflections
Reflect on this activity by answering the following questions:
 - Did you have any issues or challenges with the scans?
 - How did you overcome them?
 - How will they affect your final report?

---

### Reference
[Instructions on using traceroute, etc](https://www.a2hosting.com/kb/getting-started-guide/internet-and-networking/troubleshooting-network-connectivity-with-ping-and-traceroute/). 

---

[Return to Module 3 Unit 3](NS_Unit03.md)
