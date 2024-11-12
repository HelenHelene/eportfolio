# Team Discussion: What is a Secure Programming Language?

## Requirement
Read Chapter 2,6,7,8 of the course text (Pillai, 2017) and [Cifuentes & Bierman (2019)](SSD_Unit03_TeamActivityReference.pdf) and then answer the questions below:

### 1. What factors determine whether a programming language is secure or not?
According to Cifuentes and Bierman (2019), a secure programming language should address common vulnerabilities such as:
 - **Memory Safety:** Prevents buffer overflows and memory corruption.
 - **Type Safety:** Ensures operations are performed on compatible data types.
 - **Concurrency Support:** Manages race conditions safely.
 - **Error Handling:** Provides robust exception handling.
 - **Standard Libraries:** Includes secure defaults for cryptography and input validation.
 - **Community and Ecosystem:** Active support for security updates and patches.
 - **Tooling:** Availability of static analysis tools to detect vulnerabilities.
   
### 2. Could Python be classed as a secure language? Justify your answer.
Python has several features that contribute to its security:
 - **Memory Management:** Automatic memory management helps prevent buffer overflows.
 - **Strong Typing:** Reduces type-related vulnerabilities.
 - **Extensive Libraries:** Includes libraries for secure web development and cryptography.
 - **Community and Support:** Large community actively maintains security updates.
 - **Readability:** Encourages writing clear and maintainable code, reducing bugs.

While Python offers many secure features, it still depends on how developers use it. Misuse of functions like eval or insecure third-party libraries can introduce vulnerabilities (Pillai, 2017).

### 3. Python would be a better language to create operating systems than C. Discuss.
While Python provides high-level abstractions and ease of development, C is generally more suitable for creating operating systems due to:
 - **Performance:** C offers low-level access and efficient execution, crucial for OS development.
 - **Control:** C allows direct manipulation of hardware, essential for managing system resources.
 - **Legacy and Compatibility:** Many existing OS components are written in C, ensuring compatibility.

Python's abstractions and slower execution make it less ideal for OS development compared to C.


## Reflections
From the analysis of programming language security, I've learned that a secure language must address common vulnerabilities like memory safety, type safety, and robust error handling. Python demonstrates many secure attributes, such as automatic memory management and strong typing, which help mitigate security risks. However, it also emphasizes the importance of how developers use these features to maintain security.

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
