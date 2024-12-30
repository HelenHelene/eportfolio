# Unit 4: Exploring Programming Language Concepts

This week, we investigated and explored the effect of key programming concepts on system security. We focused on two concepts in particular: regular expressions and recursion. By examining their use in creating software solutions, we were able to identify their strengths and limitations, as well as investigate the most suitable approaches for given security requirements and risk appetites.

### Learning Outcomes
On completion of this unit, we were able to:
 - Explain how and when to use regular expressions in solutions.
 - Describe how and when to use recursion in solutions.
 - Discuss the security implications of both approaches.

### Artefacts 
As part of my e-portfolio, I have completed the following activities, which are documented in the provided link:

[Programming language concepts](SSD_Unit04_Component.md)

[Programming exercises - recursion and regex](SSD_Unit04_Seminar.md)

### Reflections
During Unit 4, I gained valuable insights into the application of regular expressions (regex) and recursion, particularly in relation to their impact on system security. These two programming concepts play a significant role in creating efficient, robust, and secure software solutions, but they also come with unique challenges that must be addressed to avoid introducing vulnerabilities into a system.

Through the artefacts, I explored how regex can be a powerful tool for input validation, such as verifying UK postcodes. Writing efficient regex patterns allowed me to validate text formats effectively while understanding the risks of "Evil Regex" attacks, such as catastrophic backtracking. This highlighted the importance of creating simple and specific regex patterns, validating input length, and incorporating additional measures like timeouts for regex operations to prevent denial-of-service (DoS) attacks. I also learned that while regex is excellent for checking input format, it should be paired with other validation techniques to ensure real-world accuracy and security.

The recursion programming exercise, specifically the Towers of Hanoi problem, provided me with a deeper understanding of how recursion works and its practical applications. By implementing a Python program that calculates the minimum number of moves required to solve the problem, I saw firsthand how recursion breaks down complex problems into smaller, manageable steps. However, I also encountered system limitations such as recursion depth, memory usage, and exponential execution time, which underscored the potential risks of stack overflow and DoS attacks in poorly implemented recursive algorithms. This emphasised the importance of optimising recursive solutions and validating user input to prevent excessive resource consumption.

These exercises also gave me a better appreciation of the security implications associated with both concepts. For regex, I learned how poorly designed patterns could be exploited, while for recursion, I became aware of the risks of infinite looping and resource exhaustion. Both require careful implementation and testing to ensure they do not become points of failure or vulnerability in a system.

Overall, Unit 4 has equipped me with the knowledge to use regex and recursion effectively while understanding their limitations and risks. I now recognise the importance of balancing functionality and security, especially when developing software that involves complex inputs or recursive logic.

### Action Plan
To further enhance my understanding, I plan to practise creating more advanced regex patterns, focusing on real-world use cases such as password validation and data sanitisation. Additionally, I intend to explore libraries that support regex timeouts, helping to minimise the risk of Evil Regex attacks.

I will incorporate layered validation techniques into my projects by combining regex with additional checks to ensure both the format and real-world accuracy of inputs.

To apply security best practices, I will remain informed about emerging security implications and implement measures such as input length limits, code reviews, and peer testing. These steps will help ensure the secure implementation of regex and recursion in my projects.

By following this action plan, I aim to strengthen my ability to create secure and efficient software solutions, effectively applying the lessons learned in Unit 4 to both academic projects and future professional work.

<br><br>

--- 

[Return to Module 6 Main Page](SSD_main.md)
