

```python
# Exercise 16.3 

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

"""Replace the if statement in rough draft with while statements"""

def increment(time, seconds):
    time.second += seconds

    while time.second >= 60:
        time.second -= 60
        time.minute += 1

    while time.minute >= 60:
        time.minute -= 60
        time.hour += 1


# Create a Time object
current_time = Time(9, 45, 0)

# Increment the time by 190 seconds (3 minute and 10 second)
increment(current_time, 190)

# Print the updated time
print_time(current_time)

```

    09:48:10



```python

```
