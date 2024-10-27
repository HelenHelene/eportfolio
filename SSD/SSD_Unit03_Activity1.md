# Activity - Exploring Python tools and features

## Part I
In this example, you will compile and run a program in C using the Jupyter notebook workspace provided (Buffer Overflow in C). The program is already provided as bufoverflow.c - a simple program that creates a buffer and then asks you for a name, and prints it back out to the screen.

This is the code in bufoverflow.c. You are able to download the zip file **'buffer-overflow-in-c'**. 
Additional instructions are provided in the [Buffer Overflow PDF](SSD_Unit03_Activity1Reference.pdf).

```python
#include <stdio.h> 
int main(int argc, char **argv)
{
char buf[8]; // buffer for eight characters
printf("enter name:"); 
gets(buf); // read from stdio (sensitive function!)
printf("%s\n", buf); // print out data stored in buf
return 0; // 0 as return value
{
```

Now compile and run the code. To test it, enter your first name (or at least the first 8 characters of it) you should get the output which is just your name repeated back to you.

Run the code a second time (from the command window this can be achieved by entering ./bufoverflow on the command line). This time, enter a string of 10 or more characters.

 - What happens?
 - What does the output message mean?

--- 

## Part II
Now carry out a comparison of this code with one in Python (Buffer Overflow in Python), following these instructions:

In your workspace, you will be using the file called Overflow.py. You are able to download the zip file **'buffer-overflow-in-python'** along with additional instructions in the PDF [Exploring Python Tools and Features](SSD_Unit03_Activity1Reference2.pdf).

```python
buffer=[None]*10
for i in range (0,11):
    buffer[i]=7
print(buffer)
```

 - Run your code using: Python overflow.py (or use the codio rocket icon)
 - What is the result?
 - Read about Pylint at http://pylint.pycqa.org/en/latest/tutorial.html
 - Install pylint using the following commands:<br>
   * _pip install pylint (in the command shell/ interpreter)_ <br>
 - Run pylint on one of your files and evaluate the output:<br>
   * _pylint your_file_ <br>
 - (Make sure you are in the directory where your file is located before running Pylint)
 - What is the result? Does this tell you how to fix the error above?

Be prepared to discuss your thoughts on both exercises at next week’s seminar. Remember to record this into your e-portfolio.


## Reflections
xxx

<br><br>

---

## Reference
xxx

<br><br>

---

[Return to Module 6 Unit 3](SSD_Unit03.md)
