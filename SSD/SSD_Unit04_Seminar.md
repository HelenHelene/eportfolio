# Programming language concepts: Programming exercises – recursion and regex

## Requirement
Please note that the Jupyter Notebook environment is available in Codio for you to carry out these activities. 
This week there are two programming exercises that will help you understand two valuable language concepts – **recursion and regex**.

## Recursion
One of the classic programming problems that is often solved by recursion is the towers of Hanoi problem. 
A good explanation and walkthrough are provided by [Cormen & Balkcom (n.d.)](https://www.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/a/towers-of-hanoi). (the code they used for their visual example is provided on their website as well).

### Read the explanation, study the code and then create your own version using Python. Create a version that asks for the number of disks and then executes the moves, and then finally displays the number of moves executed.
<img src="SSD_Unit04_Recursion1.jpg" alt="Recursion program" width="700"/> <br>

<img src="SSD_Unit04_Recursion2.jpg" alt="Recursion program input and output - 3 disks" width="500"/> <br>

<img src="SSD_Unit04_Recursion3.jpg" alt="Recursion program input - 20 disks" width="350"/> <br>

<img src="SSD_Unit04_Recursion4.jpg" alt="Recursion program output - 20 disks" width="350"/> <br>


### What is the (theoretical) maximum number of disks that your program can move without generating an error?

In the Python Official Documentation - sys Module (Python, N.D.), the getrecursionlimit() function is described as follows:

' **sys.getrecursionlimit()** <br>
Return the current value of the recursion limit, the maximum depth of the Python interpreter stack. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python. It can be set by _setrecursionlimit()_. '

' **sys.setrecursionlimit(limit)** <br>
Set the maximum depth of the Python interpreter stack to limit. This limit prevents infinite recursion from causing an overflow of the C stack and crashing Python.
The highest possible limit is platform-dependent. A user may need to set the limit higher when they have a program that requires deep recursion and a platform that supports a higher limit. This should be done with care, because a too-high limit can lead to a crash.
If the new limit is too low at the current recursion depth, a RecursionError exception is raised. '

The Python's default recursion limit is 1000 (Python Central, 2023).
This can be checked using:

This can be checked using:

```python
import sys
print(sys.getrecursionlimit())
```

### What limits the number of iterations? What is the implication for application and system security?

<br>

---

## Regex
The second language concept we will look at is regular expressions (regex). 
We have already presented some studies on their use, and potential problems, above. 
The lecturecast also contains a useful link to a tutorial on creating regex. 
Re-read the provided links and tutorial [(Jaiswal, 2020)](https://www.datacamp.com/tutorial/python-regular-expression-tutorial) and then attempt the problem presented below:

 - The UK postcode system consists of a string that contains a number of characters and numbers – a typical example is ST7 9HV (this is not valid – see below for why). The rules for the pattern are available from idealpostcodes (2020).
 - Create a python program that implements a regex that complies with the rules provided above – test it against the examples provided.
 - Examples:
      - M1 1AA
      - M60 1NW
      - CR2 6XH
      - DN55 1PT
      - W1A 1HQ
      - EC1A 1BB
- How do you ensure your solution is not subject to an evil regex attack?





## Reflections
xxx

<br><br>

---

## Reference
Cormen, T. & Balkcom, D. (N.D.) Khan Academy: Towers of Hanoi. Available from: https://www.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/a/towers-of-hanoi

Jaiswal, S. (2020) Python Regular Expression Tutorial. Available from: https://www.datacamp.com/tutorial/python-regular-expression-tutorial

Python (N.D.) sys — System-specific parameters and functions. Available from: https://docs.python.org/3/library/sys.html#sys.getrecursionlimit

Python Central (2023) Resetting the Recursion Limit. Available from: https://www.pythoncentral.io/resetting-the-recursion-limit

<br><br>

---

[Return to Module 6 Unit 4](SSD_Unit04.md)
