# Cryptography Programming Exercise

## Requirement
Read the [Cryptography with Python blog at tutorialspoint.com](https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm). 
Select one of the methods described / examples given and create a python program that can take a short piece of text and encrypt it.

## Select one of the methods described / examples given.
Before selecting a method and creating the Python program, I created a table to review all the methods described on Tutorialspoint.com.

| **Method**  | **Type**   | **Key Management**   | **Use Case**                                                                                   | **GDPR Compliance** | **Performance**               | **Weakness**                                                                                               | **Ease of Implementation**       |
| : --------------------------------|--------------------------|-------------------------------------|------------------------------------------------------------------------------------------------|----------------------|--------------------------------|------------------------------------------------------------------------------------------------------------|----------------------------------|
| **Reverse Cipher**             | Substitution Cipher      | No key required                    | Simple encryption for educational purposes                                                    | No                   | High (Fast)                   | Extremely weak; easily reversible (not secure)                                                             | Very Easy                        |
| **Caesar Cipher**              | Substitution Cipher      | Single key (shared)                | Encoding small text, educational purposes                                                     | No                   | High (Fast)                   | Vulnerable to brute force (only 25 possible keys)                                                          | Very Easy                        |
| **ROT13 Algorithm**            | Substitution Cipher      | No key required (fixed shift of 13) | Simple encoding, educational purposes                                                         | No                   | High (Fast)                   | Fixed shift makes it easily reversible; not secure                                                         | Very Easy                        |
| **Transposition Cipher**       | Rearrangement Cipher     | Single key (shared)                | Securing small text by rearranging characters                                                 | No                   | Moderate                      | Vulnerable to frequency analysis; not suitable for modern secure communication                             | Moderate                         |
| **Base64 Encoding**            | Encoding (Not Encryption)| No key required                    | Encoding binary data into text for transmission                                               | No                   | High (Fast)                   | Not encryption; easily decoded by anyone                                                                  | Easy                             |
| **XOR Process**                | Symmetric Cipher         | Single key (shared)                | Fast encryption for small data                                                                 | No                   | High (Fast)                   | Vulnerable to key reuse attacks; not secure for sensitive data                                             | Easy                             |
| **Multiplicative Cipher**      | Substitution Cipher      | Single key (shared)                | Educational purposes                                                                           | No                   | High (Fast)                   | Vulnerable to brute force; weak unless combined with other methods                                         | Moderate                         |
| **Affine Cipher**              | Hybrid Substitution      | Single key (shared)                | Basic encryption combining multiplicative and Caesar ciphers                                   | No                   | High (Fast)                   | Weak against frequency analysis unless used with strong parameters                                         | Moderate                         |
| **Monoalphabetic Cipher**      | Substitution Cipher      | Single key (substitution map)      | Encrypting text with a fixed substitution alphabet                                            | No                   | Moderate                      | Vulnerable to frequency analysis; substitution alphabet can be guessed                                     | Moderate                         |
| **Simple Substitution Cipher** | Substitution Cipher      | Single key (random substitution map)| Encrypting small text with a user-defined substitution alphabet                               | No                   | Moderate                      | Requires a secure random substitution alphabet; vulnerable to frequency analysis                          | Moderate                         |
| **Vigenere Cipher**            | Polyalphabetic Cipher    | Single key (shared)                | Encrypting text with a repeating key                                                          | No                   | Moderate (Better than Caesar) | Repeated key makes it vulnerable to statistical attacks (e.g., Kasiski examination)                        | Moderate                         |
| **One-Time Pad Cipher**        | Polyalphabetic Cipher    | Single-use key (same size as data) | Encrypting highly sensitive data (perfect secrecy if used correctly)                          | Yes                  | High (Fast)                   | Requires truly random keys as long as the plaintext; impractical for large-scale use                       | Moderate                         |
| **Data Encryption Standard (DES)** | Symmetric Cipher         | Single key (shared)                | Encrypting small data (outdated but educational)                                               | No                   | Moderate                      | Considered insecure due to small key size (56 bits); vulnerable to brute force                            | Moderate                         |
| **AES (Advanced Encryption Standard)** | Symmetric Cipher         | Single key (shared)                | Encrypting files, large amounts of data                                                       | Yes                  | High (Very Fast)              | Secure only if key is managed properly; vulnerable to side-channel attacks in flawed implementations       | Easy (with libraries like `cryptography`) |
| **RSA (Rivest–Shamir–Adleman)**| Asymmetric Cipher        | Key pair (public/private)          | Secure key exchange, digital signatures, encrypting small data                                | Yes                  | Low (Slow for large data)     | Computationally intensive; quantum computers can potentially break it in the future                       | Moderate                         |
| **Hybrid Cryptography**        | Mixed (Symmetric + Asymmetric) | Symmetric key + RSA for key exchange | Combining fast symmetric encryption (e.g., AES) with secure key exchange (e.g., RSA)           | Yes                  | High (Efficient for large data)| Complex implementation; depends on the security of the underlying symmetric and asymmetric algorithms      | Moderate to Difficult            |

## Create a python program that can take a text file and output an encrypted version as a file in your folder on the system. 


## Answer the following questions in your e-portfolio:

### Why did you select the algorithm you chose?

### Would it meet the GDPR regulations? Justify your answer.




## Reflections
xxx

<br><br>

---

## Reference
Tutorialspoint. (N.D.) Cryptography with Python - Overview. Available from: https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_quick_guide.htm

<br><br>

---

[Return to Module 6 Unit 8](SSD_Unit08.md)
