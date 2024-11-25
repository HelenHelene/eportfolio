# Exploring the Cyclomatic Complexity’s Relevance Today

## Requirement
The Cyclomatic Complexity is commonly considered in modules on testing the validity of code design today.  Justify opinions on 1. Should it be? 2. Does it remain relevant today? and 3. Is it relevant in our quest to develop secure software? 

## Introdution
Cyclomatic Complexity (CC) is a metric used to measure the complexity of a program by quantifying the number of linearly independent paths through its source code. It's calculated based on the program's control flow graph and serves as an indicator of a program's complexity (Pressman, 2010). A higher CC value indicates greater complexity, which can make the code harder to understand, test, and maintain.

### 1. Should CC be considered?

CC is a useful metric for assessing potential risks in the code. A higher complexity often correlates with a higher chance of defects and maintenance difficulties. Modules with lower CC are generally easier to understand and maintain, which is crucial for long-term project sustainability.

CC also helps in determining the minimum number of test cases needed to cover all paths in the code, ensuring thorough testing. However, with the rise of modern development practices and architectural changes, the focus has shifted towards different complexity aspects, such as system interactions rather than just code logic.

In an educational context, it's important to teach foundational concepts like CC while also introducing students to its limitations and alternative metrics. This balanced approach can provide a more holistic understanding of code complexity.

<br><br>


### 2. Is Cyclomatic Complexity remain relevant today?

It depends on the context. CC serves as a foundation for more advanced complexity metrics. Knowledge of CC enables developers to grasp more complex concepts in software metrics. However, CC only measures control flow complexity and doesn't account for other complexity types like data complexity, cognitive complexity, or the complexity introduced by modern programming paradigms.

Modern programming languages and paradigms may not be accurately assessed by CC. Nevertheless, while CC may not capture all facets of modern software complexity, it remains a relevant tool, especially when used in conjunction with other metrics. It can provide valuable insights into certain aspects of code quality and maintainability.

<br><br>

### 3. Is it relevant in our quest to develop secure software?

As CC serves as a code quality indicator. Higher CC can indicate areas of the code that are more error-prone. Security vulnerabilities often stem from code defects; thus, identifying complex code can help in targeting security reviews. Simplifying complex code can reduce the attack surface, as less complex code is generally easier to audit and secure.

CC can aid in risk assessment by helping to prioritize security testing efforts on more complex modules. However, relying solely on CC may overlook security issues in simple code or complex security requirements that aren't reflected in the cyclomatic complexity.

While CC can be a helpful indicator in identifying potentially vulnerable areas due to complexity, it should not be the sole metric relied upon for security. It's beneficial when used as part of a broader set of security analysis tools and practices.

## Conclusion
While not the sole metric to rely on, CC provides valuable insights into code structure and potential risks. It is a useful tool in the broader strategy of developing secure, maintainable software. Incorporating CC alongside other metrics and modern practices can enhance code quality and security.

## Reflections
Through exploring the relevance of CC, I have learned that while CC is not a comprehensive measure of code complexity, it remains a valuable tool for identifying potential problem areas in code. By understanding CC, I can better assess the complexity of my own code during exercises and projects.

In my coding exercises in the future, I can apply this knowledge by calculating the CC of my functions and modules to ensure they remain manageable. If I notice a high CC value, I can refactor the code to simplify control structures, thereby improving readability, maintainability, and possibly reducing the risk of defects. Additionally, being aware of CC can help me in writing more effective test cases by identifying all the independent paths that need to be tested.

<br><br>

---

## Reference

Brainhub (2024) Cyclomatic Complexity 101: Benefits, Drawbacks & Best Practices. Available from: https://brainhub.eu/library/measuring-cyclomatic-complexity  

Eland, M. (2019) Cyclomatic Complexity is the Mind Killer, Kill All Defects. Available from: https://killalldefects.com/2019/10/25/cyclomatic-complexity-and-cognitive-complexity/

Feigenspan, J., Kästner, C., Liebig, J., Apel, S. and Hanenberg, S., 2012, June. Measuring programming experience. In 2012 20th IEEE international conference on program comprehension (ICPC) (pp. 73-82). IEEE.

Ikerionwu, C., 2010. CYCLOMATIC COMPLEXITY AS A SOFTWARE METRIC. International Journal of Academic Research, 2(3).

McCabe, T.J., 1976. A complexity measure. IEEE Transactions on software Engineering, (4), pp.308-320.

Pressman, R. S. (2010). Software Engineering: A Practitioner's Approach. 7th ed. New York: McGraw-Hill.

<br><br>

---

[Return to Module 6 Unit 5](SSD_Unit05.md)
