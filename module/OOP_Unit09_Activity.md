###  Extend the program to test accuracy of operations using the assert statement.

#### Original program
```python
# Python String Operations
str1 = 'Hello'
str2 ='World!'

# using +
print('str1 + str2 = ', str1 + str2)

# using *
print('str1 * 3 =', str1 * 3)
```

#### Extended program

```python
# Python String Operations
str1 = 'Hello'
str2 = 'World!'

# using +
result_concat = str1 + str2
print('str1 + str2 =', result_concat)
assert result_concat == 'HelloWorld!', "Concatenation failed"

# using *
result_repeat = str1 * 3
print('str1 * 3 =', result_repeat)
assert result_repeat == 'HelloHelloHello', "Repetition failed"

print("All tests passed.")
```


#### Explanation

Concatenation Test:
 - result_concat stores the result of concatenating str1 and str2.
 - The assert statement checks if the result is 'HelloWorld!'.

Repetition Test:
 - result_repeat stores the result of repeating str1 three times.
 - The assert statement checks if the result is 'HelloHelloHello'.

Output:
 - If all assertions pass, "All tests passed." will be printed.
 - If any assertion fails, an AssertionError with the specified message will be raised.

---

[Return to Module 2 Unit 9](OOP_Unit09.md)

