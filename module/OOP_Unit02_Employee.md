
```python
# Employee Management Program

"""Write a Python program to achieve basic employee-related functionality,
which includes retaining employee details and allowing an employee to book a day of annual leave. 
Extend the Python program you have now created to use protected and unprotected variables."""

class Employee:
    """
    Represents an employee with basic details and annual leave management.
    """

    def __init__(self, name, employee_id, annual_leave_days):
        """Initializes an Employee instance."""
        self.name = name  # Public variable for the employee's name
        self.employee_id = employee_id  # Public variable for the employee's ID
        self._annual_leave_days = annual_leave_days  # Protected variable for available leave days

    def get_details(self):
        """Returns the employee's details."""
        return f"Employee: {self.name}, ID: {self.employee_id}, Annual Leave Days: {self._annual_leave_days}"

    def book_leave(self, days):
        """Books a specified number of leave days."""
        if days <= 0:
            print("Number of leave days must be positive.")
            return False

        if days > self._annual_leave_days:
            print("Not enough annual leave days available.")
            return False

        self._annual_leave_days -= days
        print(f"Leave booked for {days} days. Remaining leave days: {self._annual_leave_days}")
        return True

# Example usage
employee1 = Employee("Alice", "E001", 20)

# Accessing and displaying employee details
print(employee1.get_details())

# Booking 5 days of leave
employee1.book_leave(5)

# Trying to book more leave than available
employee1.book_leave(17)

# Trying to book a negative number of days
employee1.book_leave(-3)
```

```python
# Employee Management Program Output

Employee: Alice, ID: E001, Annual Leave Days: 20
Leave booked for 5 days. Remaining leave days: 15
Not enough annual leave days available.
Number of leave days must be positive.
```

---

[Return to Module 2 Unit 2](OOP_Unit02.md)
