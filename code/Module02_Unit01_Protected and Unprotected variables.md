

```python
# Unit01 e-Portfolio Activities
# Develop a Python program and apply protected and unprotected variables within it.

# Defining a class 
class Staff:
    def __init__(self, _id, name):
        self._id = _id  # Protected variable 
        self.name = name  # Unprotected variable

    def __str__(self):
        return "ID: {}\nName: {}".format(self._id, self.name)

# Create an instance of Staff
staff_member = Staff(123, "Amy")

# Access protected variable
print("Protected variable _id:", staff_member._id)

# Access unprotected variable
print("Unprotected variable name:", staff_member.name)

# Update protected variable
staff_member._id = 456
print("Updated protected variable _id:", staff_member._id)

# Update unprotected variable
staff_member.name = "Barry"
print("Updated unprotected variable name:", staff_member.name)

# Print staff details
print(staff_member)
```

    Protected variable _id: 123
    Unprotected variable name: Amy
    Updated protected variable _id: 456
    Updated unprotected variable name: Barry
    ID: 456
    Name: Barry



```python

```
