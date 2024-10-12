# Seminar Preparation: Estimating Tools and Risk Assessment

## Task 1: Review of NIST Privacy Tools
The [NIST Privacy tools](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/resources), such as the **Privacy Risk Assessment Methodology (PRAM)**, are designed to help organizations identify and manage privacy risks. These tools align well with risk assessment methods as they provide a structured approach to analyzing privacy risks and determining appropriate responses. By applying systems engineering practices, organizations can integrate privacy considerations into their risk assessments, ensuring that privacy risks are considered alongside other types of risks.
<br><br>

## Task 2: Python Program for Estimation
Given that the project timeline is 13 months as per the requirements from Assignment 1.  Below is a Python program that implements the estimation method from the **Mythical Man Month**.  It calculates the total effort and time based on the formula, assuming that T is the total time allowed for the project:<br>
<br>

**Tc = Tp + Td + Tt + Ts** (Brooks, 1995) 
 - Tc = Time to complete the project.
 - Tp = Planning time (T/3).
 - Td = development time (T/6).
 - Tt = Testing time (T/6).
 - Ts = System test time (T/4).

```python
# Unit 4 - Implements the estimation method from the Mythical Man Month. 

def estimate_project_time(T):
    Tp = T / 3  # Planning time (T/3)
    Td = T / 6  # development time (T/6)
    Tt = T / 6  # Testing time (T/6)
    Ts = T / 4  # System test time (T/4)
    Tc = Tp + Td + Tt + Ts  # Time to complete the project.
    return Tc, Tp, Td, Tt, Ts

# Example usage
T = 13  # Total time allowed in months as per Assignment 1
Tc, Tp, Td, Tt, Ts = estimate_project_time(T)

print(f"Total time to complete the project (Tc): {Tc} months")
print(f"Planning time (Tp): {Tp} months")
print(f"Development time (Td): {Td} months")
print(f"Testing time (Tt): {Tt} months")
print(f"System test time (Ts): {Ts} months")
```

```python
# Unit 4 Output

Total time to complete the project (Tc): 11.916666666666666 months
Planning time (Tp): 4.333333333333333 months
Development time (Td): 2.1666666666666665 months
Testing time (Tt): 2.1666666666666665 months
System test time (Ts): 3.25 months
````

Using the Python program, since the sum of the above values is less than 13, and studies show that inadequate quality control is one of the major contributors to project failures (Jones, 2004), the additional time will be devoted to testing, bringing it up to 3.2 months. 

The breakdown is as follows:
Total time to complete the project (Tc): 13 months
Planning time (Tp): 4.33 months
Development time (Td): 2.17 months
Testing time (Tt): 2.17 months
System test time (Ts): 3.25 months

These estimates help ensure that the project stays on track by allocating appropriate time for each phase.

<br><br>

## Reflections
...

<br><br>

---

## Reference
Brooks, F.P. (1995) The Mythical Man-Month. Anniversary Edition. Philippines: Addison-Wesley. 

Jones, C. (2004) Software project management practices: Failure versus success. CrossTalk: The Journal of Defense Software Engineering, 17(10): 5-9.

Jupter. (N.D.) Try Jupyter. Available from: https://jupyter.org/try

NIST. (2024) NIST Privacy tools. Available from: https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/resources

<br><br>

---

[Return to Module 5 Unit 4](SEPM_Unit04.md)
