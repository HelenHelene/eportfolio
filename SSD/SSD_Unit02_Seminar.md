# Scrum Security review


## Question 1: Table
Create a 2-column multi-line table. In the left-hand column, include the software development stages of the Scrum agile life cycle approach to project management. In the right-hand column, describe the processes which you recommend are applied at each stage to ensure that secure software is produced at the end of the development. 

<br><br>

| **Scrum Development Stage** | **Recommended Security Processes** (Sharma & Bawa, 2020) |
| :---------------------------- | :----------------------------------- |
| **Product Backlog**         | Conduct security requirement gathering and threat modeling. Identify and prioritise security features. Use role matrix for access control definitions. |
| **Sprint Planning**         | Integrate security requirements into sprint goals. Ensure tasks include security testing and code reviews. Specify operational environment security needs. |
| **Daily Scrum**             | Include security status updates. Discuss and mitigate any security risks or issues identified during development. |
| **Sprint Review**           | Demonstrate implemented security features. Review any security vulnerabilities identified and discuss solutions. |
| **Sprint Retrospective**    | Analyse security incidents or vulnerabilities from the last sprint. Adjust processes to improve security practices. |
| **Release**               | Perform final security testing before releasing to production. Conduct penetration testing and dynamic analysis. |

### References
Sharma, A. & Bawa, RK. (2020) Identification and integration of security activities for secure agile development. DOI: https://doi.org/10.1007/s41870-020-00446-4

### Bibliography
Moyon, F. et al. (2020) How to Integrate Security Compliance Requirements with Agile Software Engineering at Scale?. DOI: 10.1007/978-3-030-64148-1_5


<br><br>

---

## Question 2: Blog Post 
Some say that people are the biggest risk of cyber security.
Select five terms from ISO/IEC Standard 27000 Section 3 Terms and Definitions and write a 300-word blog post on how people can be managed to overcome cyber security attacks from the inside.

### [Managing People to Mitigate Insider Cybersecurity Threats](SSD_Unit02_Blog.pdf)

Insider threats, often due to human error, are a significant risk in cybersecurity. Managing these threats requires a strategic approach based on the ISO/IEC 27000:2018 standard. I have chosen the following terms from ISO/IEC Standard 27000 Section 3 Terms and Definitions to explore how they can help overcome cybersecurity attacks from inside.

### 3.1 Access Control
ISO (2018) defines this as: <br>
_“means to ensure that access to assets is authorised and restricted based on business and security requirements (3.56)”_ <br>

By granting employees only the access necessary for their job functions, organisations adhere to the principle of least privilege. This minimises the risk of unauthorized access leading to data breaches or misuse of information by insiders.

### 3.9 Competence
ISO (2018) defines this as: <br>
_“ability to apply knowledge and skills to achieve intended results”_ <br>

Ensuring that all personnel have the necessary skills to perform their roles securely is vital. Organizations should invest in continuous education, such as cybersecurity awareness training. Enhancing employee competence promotes thoughtful and secure behaviour, reducing the likelihood of mistakes that could compromise security.

### 3.10 Confidentiality
ISO (2018) defines this as: <br>
_“property that information is not made available or disclosed to unauthorized individuals, entities, or processes (3.54)”_ <br>

Employees must understand the importance of safeguarding sensitive information and the potential consequences of unauthorised disclosure. By fostering a culture that values confidentiality, organizations can reduce the risk of accidental leaks and ensure appropriate handling of information. Methods to enforce confidentiality include data classification, encryption, and clear policies on data handling, aligning closely with access control (3.1) measures.

### 3.14 Control
ISO (2018) defines this as: <br>
_“measure that is modifying risk (3.61)”_ <br>

Establishing robust controls, such as segregation of duties, regular audits, monitoring systems, and incident response procedures helps detect and prevent malicious or inadvertent activities within the organization. Regularly reviewing and adjusting these controls ensures their continued effectiveness against evolving threats.

### 3.23 Governance of Information Security
ISO (2018) defines this as: <br>
_“system by which an organization’s (3.50)information security (3.28) activities are directed and controlled”_ <br>

Effective governance ensures that security strategies align with business objectives and are embedded throughout the organization. By establishing clear leadership, roles, and responsibilities, organizations create an environment where information security is everyone's responsibility. This top-down approach reinforces the importance of security policies and procedures, leading to better adherence and accountability at all levels.

### Conclusion
By focusing on these key areas defined in the ISO/IEC 27000:2018 standard, organizations can effectively mitigate risks posed by internal actors. Empowering employees with knowledge, restricting access appropriately, safeguarding sensitive information, implementing risk-modifying controls, and strategically directing security activities are all critical steps in strengthening an organization's overall security posture.

### References
ISO. (2018) ISO/IEC 27000:2018 Information technology-Security techniques-Information security management systems-Overview and vocabulary. Available from: https://www.iso.org/obp/ui/#iso:std:iso-iec:27000:ed-5:v1:en:term:3.50 [Accessed 4 November 2024].

### Bibliography
Kemp, CL. & Theoharidou, M. (2010). Insider Threat and Information Security Management. DOI: 10.1007/978-1-4419-7133-3_3

<br><br>

---


## Reflections
In the Scrum Security Review, I gained a comprehensive understanding of integrating security processes within the Scrum framework. By mapping security activities to each Scrum stage, I've learned to appreciate the importance of embedding security considerations from the outset. This approach enhances the security posture of software projects and ensures that security is an ongoing concern rather than an afterthought. Identifying and prioritizing security features early in the Product Backlog helps mitigate risks from the start. Incorporating security tasks in Sprint Planning and Daily Scrums keeps the team focused on security throughout development. Regular Sprint Reviews and Retrospectives allow the team to address vulnerabilities and refine security practices continuously.

In the Blog Post on Managing Insider Cybersecurity Threats, I explored how human factors significantly impact cybersecurity. By delving into ISO/IEC 27000 terms, I learned how to strategically manage insider risks. Implementing the principle of least privilege and cultivating a culture of confidentiality are crucial in preventing unauthorized access and data breaches. Ensuring employees are well-trained and aware of security protocols reduces the likelihood of errors that could lead to security incidents. Establishing strong governance and controls ensures that security measures align with organizational goals and are effectively implemented.

Overall, these exercises have reinforced the importance of integrating security at every stage of development and managing human elements to safeguard against insider threats. This holistic approach to security fosters a culture of awareness and responsibility, ultimately strengthening the organization’s security framework.

<br><br>

---

[Return to Module 6 Unit 2](SSD_Unit02.md)
