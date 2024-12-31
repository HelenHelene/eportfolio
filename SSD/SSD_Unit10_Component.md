# Faceted Data

## Requirement
Read Schmitz et al (2016) article about faceted data.

## What Is Faceted Data?
Faceted data is a concept used to enforce dynamic information flow security. A faceted value represents multiple views of the same piece of data, depending on the observer's privileges or security labels. This approach ensures that sensitive information is protected, even when exposed to unauthorized viewers.

Each faceted value has:
 - A private view: The actual sensitive data, visible only to authorized observers.
 - A public view: A default, nonsensitive representation of the data, visible to unauthorized observers.
   
These views are dynamically determined based on a security label that specifies who is authorized to see the sensitive data.

## Do you think this is a good approach to protect systems from data leakage? What are the pros and cons?
Yes, the faceted data approach is a promising method for protecting systems from data leakage. It provides a dynamic way to enforce information flow policies by presenting different "views" of data based on the observer’s privileges. This approach is particularly useful for maintaining confidentiality while ensuring that authorized users can access sensitive information.

Below are the Pros and Cons according to Schmitz et al (2016).

**Pros:**
1. Dynamic Handling of Sensitive Data:
    - Faceted values dynamically provide different "views" of data (private and public) based on observer privileges, offering flexibility in enforcing information flow policies.
    - This ensures consistent behavior for unauthorized viewers while protecting sensitive information.

2. Prevents Explicit and Implicit Data Leakage:
   - Explicit flows (direct assignments of sensitive data) and implicit flows (inferences through program control flow) are both addressed effectively.
   - The system dynamically tracks branching control flows using a program counter (pc) to avoid sensitive leaks.

3. No Language Runtime Modifications:
   - The approach is implemented as a library, avoiding the need for intrusive modifications to the language runtime.
   - This makes it easier to integrate into existing systems.

4. Simulates Secure Multi-Execution (SME):
   - Faceted values achieve the same guarantees as SME but with better efficiency since they avoid redundant computations by simulating multiple program executions in a single process.

5. Formal Security Guarantees:
   - The system guarantees termination-insensitive noninterference, meaning public outputs are independent of private inputs, even if errors or malicious code exist in the application.

6. Expressiveness:
   - The dual-monad design (Faceted and FIO) allows secure handling of both data flows (via faceted values) and control flows (via faceted I/O).

**Cons:**
1. Performance Overhead:
   - Simulating multiple "views" of data within a single process may lead to runtime overhead, especially for complex computations or large data sets.
   - The need to track program counter (pc) labels and simulate different branches can further add to the cost.

2. Limited Parallelization:
   - Unlike actual SME, which can run processes in parallel, faceted evaluation cannot easily take advantage of parallelism, potentially affecting scalability.

3. Complexity for Developers:
   - Integrating faceted values into an existing system may require developers to explicitly handle faceted types (Faceted, FIO) and carefully structure their programs.
   - Understanding and debugging faceted computations can be challenging.

4. Limited to Dynamic Enforcement:
   - While dynamic techniques are flexible, they may not catch all leaks at compile-time. Static or hybrid approaches may be more appropriate for systems requiring stricter guarantees.

5. Trusted Environment Assumptions:
   - Faceted I/O relies on external environments (e.g., file systems or network sockets) to enforce confidentiality labels, which may not always be reliable.


## Create a basic outline design of how you would create such a system in Python. 

Here’s a basic outline of how to create a similar system in Python:

1. Define Faceted Values
   - Represent data with multiple "views" (private and public) based on a label.

2. Define the Program Counter (pc):
   - Tracks the current security context (e.g., what sensitive labels the computation depends on).

3. Implement Faceted Reference Cells
   - Python objects (like mutable objects, files, or variables) that store faceted values, ensuring secure reads and writes.

4. Implement Faceted I/O
   - File or network operations that enforce confidentiality dynamically.

## Reflections
The faceted data model provides a robust mechanism for enforcing information flow security dynamically. While it is theoretically sound and practically useful in type-safe languages like Haskell, implementing it in Python introduces challenges such as performance overhead and runtime complexity. Despite these challenges, the flexibility and granularity of faceted data make it a valuable tool for protecting sensitive information in modern systems.

<br><br>

---

## Reference
Schmitz, T., Rhodes, D., Austin, T.H., Knowles, K., Flanagan, C. (2016) Faceted Dynamic Information Flow via Control and Data Monads. In: Piessens F., Viganò L. (eds) Principles of Security and Trust. POST 2016. Lecture Notes in Computer Science, vol 9635. Springer, Berlin, Heidelberg.


## Bibliography
K. Micinski, D. Darais and T. Gilray, "Abstracting Faceted Execution," 2020 IEEE 33rd Computer Security Foundations Symposium (CSF), Boston, MA, USA, 2020, pp. 184-198, doi: 10.1109/CSF49147.2020.00021.

Niu, X., Fan, X., & Zhang, T. (2019). Understanding faceted search from data science and human factor perspectives. ACM Transactions on Information Systems (TOIS), 37(2), 1-27. 

The Global Legal Post. (2019) Data breach needs multi-faceted approach. Available from: https://www.globallegalpost.com/news/data-breach-needs-multi45faceted-approach-45083887

Vendure. (2024) Facets. Avaiable from: https://docs.vendure.io/user-guide/catalog/facets

Wisdon, D. (2024) Best practices to prevent data leaks. Available from: https://www.datalinknetworks.net/dln_blog/best-practices-to-prevent-data-leaks 

<br><br>

---

[Return to Module 6 Unit 10](SSD_Unit10.md)
