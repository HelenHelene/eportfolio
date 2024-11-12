# Programming language concepts

## Requirement
Read [Larson (2018)](SSD_Unit04_Reference.pdf) and [Weidman (n.d.)](https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS) then answer the questions below:

### 1. What is ReDoS and what part do ‘Evil Regex’ play?
ReDoS, or Regular Expression Denial of Service, is an attack targeting weaknesses in how some regular expression (regex) engines handle input. It exploits patterns that lead to excessive backtracking, using up lots of CPU and memory, which can slow down or crash systems, denying service to real users.

'Evil Regex' patterns are key to ReDoS attacks. They can cause complex processing times due to their structure, often involving:
 - **Nested Repetitions:** Patterns like (a+)+ can make the engine try too many matches.
 - **Repetitions in Groups:** Repeated groups with more repetitions lead to numerous matching paths.
 - **Overlapping Alternation:** Using | where options can match the same prefixes, increasing processing time.

Attackers use these patterns to cause catastrophic backtracking, making the regex engine use excessive resources, leading to denial of service.

### 2. What are the common problems associated with the use of regex? How can these be mitigated?
Common regex problems include:
 - **Catastrophic Backtracking:** Poorly made regex can lead to too much backtracking and performance issues like ReDoS.
 - **Wrong Use of Character Sets:** Misunderstanding syntax can cause incorrect matches.
 - **Unbalanced Braces/Parentheses:** Optional braces can lead to unexpected inputs.
 - **Misuse of Wildcards:** Using . too freely can match unintended characters.
 - **Repeating Punctuation:** Allowing repeated punctuation can lead to invalid matches.
 - **Misplaced Anchors:** Incorrect use of ^ and $ can cause wrong matches.
 - **Duplicate Characters:** Repeated characters in sets might indicate errors.

Below are the possible mitigation strategies:
 - **Use Automated Tools:** Employ tools like ACRE to check regex patterns for mistakes.
 - **Avoid 'Evil Regex':** Be careful with nested quantifiers and ambiguous alternations.
 - **Be Specific:** Define character sets and quantifiers clearly.
 - **Test Regex Patterns:** Test regex with various inputs, including edge cases.
 - **Understand Engine Behaviour:** Know how the regex engine works.
 - **Code Reviews:** Include regex in code reviews and peer testing.
 - **Stay Updated:** Keep informed about regex best practices.

### 3. How and why could regex be used as part of a security solution?
Regex can enhance security by defining and enforcing text patterns. Uses include:
 - **Input Validation:** Ensures user input meets criteria (e.g., emails, phone numbers), preventing injection attacks.
 - **Input Sanitisation:** Removes harmful patterns before processing.
 - **Detecting Malicious Patterns:** Scans for threats in data streams and logs.
 - **Access Control:** Defines allowed patterns for filenames and URLs.
 - **Data Masking:** Identifies and hides sensitive information.
 - **Content Filtering:** Blocks unwanted content in applications and servers.

Why Use Regex for Security:
 - **Flexibility:** Regex can succinctly describe complex patterns.
 - **Efficiency:** Properly made regex can handle large text data efficiently.
 - **Integration:** Easily added to systems as most languages support regex.
 - **Automation:** Automates security pattern handling, reducing errors.

While regex is a valuable tool in security solutions, it is essential to use it carefully:
 - **Performance:** Ensure regex is optimised to avoid ReDoS vulnerabilities.
 - **Security:** Regularly review patterns to avoid flaws.
 - **Complementary Measures:** Use regex with other security practices.
 - **Limitations:** Recognise regex's limits; it's not for complex parsing.

By using regex wisely, security solutions can better manage and validate text data, improving overall security.


## Reflections
Through this Q&A, I have deepened my understanding of ReDoS attacks and the role of 'Evil Regex' patterns. I learned that ReDoS exploits inefficiencies in regex handling, leading to excessive backtracking and resource consumption. Understanding how nested repetitions and overlapping alternation contribute to these vulnerabilities is crucial.

In my future coding practice, I will focus on designing efficient regex patterns by avoiding structures that lead to excessive backtracking and being mindful of nested quantifiers and ambiguous patterns. Implementing mitigation strategies is also essential. I plan to use automated tools to detect potential regex vulnerabilities and conduct thorough testing with diverse inputs, including edge cases.

Enhancing security practices is another key takeaway. I will leverage regex for input validation and sanitisation while regularly reviewing and updating patterns to ensure security. Staying informed about best practices and updates in regex usage is vital, and I will engage in peer reviews to catch potential issues early.

By integrating these lessons into my coding workflow, I aim to write more secure and efficient code, reducing the risk of ReDoS and enhancing overall application performance.

<br><br>

---

## Reference
Larson, E. (2018) Automatic Checking of Regular Expressions. 18th IEEE International Working Conference on Source Code Analysis and Manipulation (SCAM).

Weidman, A. (n.d.) Regular expression Denial of Service - ReDoS.

<br><br>

---

[Return to Module 6 Unit 4](SSD_Unit04.md)
