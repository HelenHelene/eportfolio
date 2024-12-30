# Unit 5: An Introduction to Testing

During this unit, we explored the art of testing software, focusing on both general quality and, specifically, security. For example, we examined the range of questions to ask when developing a test plan, becoming familiar with the key concepts in software testing and understanding their relevance within the context of security. We also investigated key industry practices, including OWASP and contributions from ISO/IEC/IEEE, and explored how these standards guide software testing processes. 

### Learning Outcomes
By the end of this unit, we were able to:
 - Describe the key terms associated with testing software for security.
 - Prepare a list of questions to ask when designing a test plan for secure software.
 - Design software tests by understanding the range of ways in which the security of software can be breached.

### Artefacts 
As part of my e-portfolio, I have completed the following activities, which are documented in the provided link:

[Equivalence Testing in Python](SSD_Unit05_Activity.md)

[Exploring the Cyclomatic Complexity’s Relevance Today](SSD_Unit05_Component.md)


### Reflections
During this unit, I gained valuable insights into software testing concepts, their application in improving software security, and the practical tools available in Python to support and automate these processes. By delving into equivalence testing in Python, I learned how to group and classify data into equivalence classes using defined relations, ensuring that software tests are comprehensive yet efficient. This highlighted the importance of systematically evaluating relationships between data elements and testing edge cases to ensure robustness. From this, I now better understand how equivalence partitioning can be applied in black-box testing to reduce the number of test cases while maintaining coverage, which is invaluable for both functional and security testing.

Exploring the relevance of Cyclomatic Complexity (CC) further broadened my understanding of code quality metrics and their role in software testing. I learned that while CC is not a comprehensive measure of all types of complexity, it remains a valuable tool for identifying potentially problematic areas in the code. For example, high CC values often indicate areas prone to defects or maintenance challenges, and simplifying these areas can improve both security and readability. I also realised that CC can guide the creation of effective test cases by identifying independent paths in the code, ensuring thorough testing. However, I came to appreciate the limitations of CC, particularly in modern programming paradigms, where other complexity types (e.g., cognitive complexity) may also need to be considered to ensure secure and maintainable software.

This unit also reinforced the importance of automated tools in testing. By engaging with Python-based tools such as linters and security-focused utilities like Bandit, I now understand how these tools can assist in identifying vulnerabilities, enforcing coding standards, and improving overall code quality. This practical exposure has shown me how automation can not only save time but also enhance the accuracy and reliability of the testing process, particularly when addressing common attack surfaces.

### Action Plan
To further develop my understanding and skills in software testing, I plan to continue experimenting with equivalence partitioning by applying it to more complex, real-world scenarios, especially in security-focused testing. This will help me refine my ability to identify equivalence classes and edge cases, ensuring comprehensive testing coverage. 

I also aim to deepen my knowledge of Python’s testing tools by experimenting further with Bandit and other linters, integrating them into my development workflow. By automating the identification of stylistic and security issues, I can ensure my code adheres to best practices while minimising vulnerabilities.

<br><br>

--- 

[Return to Module 6 Main Page](SSD_main.md)
