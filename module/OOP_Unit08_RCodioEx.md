
```python
# Recursion Ex. 1
"""Write a recursive function called recursive_sum that takes an integer as a parameter.
Return the sum of all integers between 0 and the number passed to recursive_sum."""

def recursive_sum(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: return n plus the sum of all numbers before it
    else:
        return n + recursive_sum(n - 1)

# Example usage:
print(recursive_sum(5))  
print(recursive_sum(10)) 
```

```python
# Recursion Ex. 1 Output

15
55
```

---

```python
# Recursion Ex. 2
"""Write a recursive function called list_sum that takes a list of numbers as a parameter.
Return the sum of all of the numbers in the list. Hint, the slice operator will be helpful in solving this problem."""

def list_sum(numbers):
    # Base case: if the list is empty, return 0
    if not numbers:
        return 0
    # Recursive case: return the first element plus the sum of the rest of the list
    else:
        return numbers[0] + list_sum(numbers[1:])

# Example usage:
print(list_sum([1, 2, 3, 4, 5]))
print(list_sum([10, 12.5, 10, 7]))
```

```python
# Recursion Ex. 2 Output

15
39.5
```

---

```python
# Recursion Ex. 3
"""Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter.
Return the number of bunny ears (2 per bunny). Do not use multiplication; instead use addition."""

def bunny_ears(bunnies):
    # Base case: if there are no bunnies, return 0
    if bunnies == 0:
        return 0
    # Recursive case: each bunny has 2 ears plus the ears of the remaining bunnies
    else:
        return 2 + bunny_ears(bunnies - 1)

# Example usage:
print(bunny_ears(8))
print(bunny_ears(0))
```

```python
# Recursion Ex. 3 Output

16
0
```

---

```python
# Recursion Ex. 4
"""Write a recursive function called reverse_string that takes a string as a parameter.
Return the string in reverse order. Hint, the slice operator will be helpful when solving this problem."""

def reverse_string(s):
    # Base case: if the string is empty, return the empty string
    if s == "":
        return ""
    # Recursive case: return the last character plus the reverse of the rest of the string
    else:
        return s[-1] + reverse_string(s[:-1])

# Example usage:
print(reverse_string("cat"))
print(reverse_string("house")) 
```

```python
# Recursion Ex. 4 Output

tac
esuoh
```

---

```python
# Recursion Ex. 5
"""Write a recursive function called get_max that takes a list of numbers as a parameter. Return the largest number in the list."""

def get_max(numbers):
    # Base case: if the list contains only one element, return that element
    if len(numbers) == 1:
        return numbers[0]
    # Recursive case: compare the first element with the maximum of the rest of the list
    else:
        max_of_rest = get_max(numbers[1:])
        return max(numbers[0], max_of_rest)

# Example usage:
print(get_max([1, 2, 3, 4, 5]))
print(get_max([11, 22, 3, 41, 15]))
```

```python
# Recursion Ex. 5 Output

5
41
```

---

[Return to Module 2 Unit 8](OOP_Unit08.md)
