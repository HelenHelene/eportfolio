

```python
# exercise 16.1 

"""Represents the time of day.
    attributes: hour, minute, second"""

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        
"""Write a function called print_time that takes a Time object and
    prints it in the form hour:minute:second."""   

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))

# Create Time object
t1 = Time(11, 59, 30)

# Print Time object
print_time(t1)


"""Write a boolean function called is_after that takes two Time objects, t1 and t2, 
and returns True if t1 follows t2 chronologically and False otherwise.  Dont's use an if statement"""

def is_after(t1, t2):
    #Converted to second
    return (t1.hour * 3600 + t1.minute * 60 + t1.second) > (t2.hour * 3600 + t2.minute * 60 + t2.second)

# Create Time objects
t1 = Time(11, 59, 45)
t2 = Time(12, 0, 0)

# Print Time objects
print_time(t1)
print_time(t2)

# Check if t1 is after t2
print(is_after(t1, t2))
  

```

```python
# Output
    11:59:30
    11:59:45
    12:00:00
    False

```
