# Team Discussion: What is a Secure Programming Language?

## Requirement
Read Chapter 2,6,7,8 of the course text (Pillai, 2017) and Cifuentes & Bierman (2019) and then answer the questions below:

### 1. What factors determine whether a programming language is secure or not?
According to Cifuentes and Bierman (2019), a secure programming language should address common vulnerabilities such as:
 - **Buffer Errors:** These occur when a program overruns the buffer's boundary and overwrites adjacent memory, leading to crashes or exploitable code execution. A secure language should prevent buffer overflows by managing memory safely.
 - **Injection Errors:** Such as SQL injection or cross-site scripting (XSS), these happen when untrusted input is incorporated into code or commands executed by the program. Secure languages should provide abstractions that eliminate the risks of code injection by properly handling and sanitizing user inputs.
 - **Information Leak Errors:** These vulnerabilities involve the unintended disclosure of sensitive information. A secure language should ensure that sensitive data is handled correctly and not exposed to unauthorized entities.

Pillai (2017) indirectly touches upon security through discussions of modifiability, readability, and testability. These qualities, while not directly security features, contribute to a more secure development process by reducing the likelihood of vulnerabilities.
   
### 2. Could Python be classed as a secure language? Justify your answer.
Python has several features that contribute to its security:
 - **Memory Management:** Python's automatic garbage collection helps prevent memory leaks and dangling pointers, reducing the risk of memory-related vulnerabilities.
 - **Type Safety:** While dynamically typed, Python enforces type checking at runtime, catching potential type-related errors that could lead to security issues.
 - **Community and Ecosystem:** Python has a large and active community that emphasizes secure coding practices. Numerous security-focused libraries and tools are readily available.

Overall, Python is considered relatively secure, but it still depends on how developers use it. Misuse of functions like eval or insecure third-party libraries can introduce vulnerabilities. 
Pillai (2017) suggests several strategies for enhancing security when using Python:
 - **Input Validation:** Always validate user input using raw_input() (Python 2) or input() (Python 3) and handle type conversions manually. Use getpass for passwords.
 - **Avoid eval() and exec():** Never use these functions with untrusted input. If absolutely necessary, restrict their use to controlled and trusted data sources.
 - **Safe Serialization:** Avoid pickle and cPickle. Use json or yaml instead. If pickle is unavoidable, implement sandboxing or chroot jails.
 - **Handle Integer Overflows:** Use exception handlers to catch and manage potential integer overflows.
 - **Secure String Formatting:** Use the format() method for string formatting instead of the older % operator to prevent format string vulnerabilities.

### 3. Python would be a better language to create operating systems (OS) than C. Discuss.
While Python provides high-level abstractions and ease of development, C is generally more suitable for creating OS due to:
 - **Performance:** C offers low-level access and efficient execution, crucial for OS development which require high performance for efficient resource management.
 - **Control:** C offers precise control over hardware resources while Python's higher-level abstractions limit this control.
 - **Existing Ecosystem:** The vast majority of existing operating systems are written in C or C++, creating a mature ecosystem of tools and libraries specifically designed for OS development.

While Python excels in application development due to its simplicity and productivity, it is not suitable for creating OS where performance, resource management, and hardware interaction are paramount (Cifuentes & Bierman, 2019). Therefore, C remains the preferred choice for OS development.

## Reflections
From the analysis of programming language security, I've learned that a secure language must address common vulnerabilities like memory safety, type safety, and robust error handling. Python demonstrates many secure attributes, such as automatic memory management and strong typing, which help mitigate security risks. However, it also emphasises the importance of how developers use these features to maintain security.

Python's high-level nature and readability make it ideal for tasks requiring rapid development, but it lacks the low-level control and performance efficiency needed for operating systems, which C provides.

In my upcoming coding assignment, I can apply these insights by:
 - Utilizing Python's secure libraries and adhering to best practices to ensure code safety.
 - Avoiding functions like eval that could introduce vulnerabilities.
 - Ensuring proper input validation and error handling to prevent common security issues.
 - Focusing on writing clear and maintainable code to reduce bugs and improve security.
By leveraging Python's strengths and being mindful of potential pitfalls, I can create more secure and reliable software.

<br><br>

---

## Reference
Cifuentes, C. & Bierman, G. (2019) What is a Secure Programming Language? 3rd Summit on Advances in Programming Languages (SNAPL).136(3): 1 - 15.

Pillai, A.B. (2017) Software Architecture with Python. Birmingham, UK. Packt Publishing Ltd.

<br><br>

---

[Return to Module 6 Unit 3](SSD_Unit03.md)
