

```python
# Exercise 17.2 

"""Class and Function

# Define class
class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
# Define funtion
def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

# Create Time object
start = Time(9, 45, 0)

# Print Time object = says "Hey print_time! Here's an object for you to print.”
print_time(start)"""


"""Method: Move function definition inside the class definition"""

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
          
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

# Create Time object
start1 = Time(9, 50, 0)
start2 = Time(10, 20, 10)

# Print Time object =  "Hey start! Please print yourself.”
start1.print_time()
start2.print_time()

```

```python
# Output
    09:50:00
    10:20:10

```
