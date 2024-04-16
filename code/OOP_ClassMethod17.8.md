

```python
#Session 17.8

class Time:
    #Define Time class 
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    # Define the __add__ method for addition
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    # Define the add_time method for adding two Time objects
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return Time.int_to_time(seconds)
   
    # Define the increment method for adding seconds to a Time object
    def increment(self, seconds):
        seconds += self.time_to_int()
        return Time.int_to_time(seconds)
    
    # Define the print_time method to print the time in the desired format
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    # Define the time_to_int method to convert Time to seconds
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds
   
    # Define the int_to_time static method to convert seconds to a Time object
    @staticmethod
    def int_to_time(seconds):
        time = Time(0, 0, 0)
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

# Create Time objects
start = Time(9, 45, 0)
duration = Time(1, 35, 0)

# Print the result of adding start and duration
result1 = start + duration
result1.print_time()

# Print the result of adding start and 1337 seconds
result2 = start + 1337
result2.print_time()
```

```python
# Output

    11:20:00
    10:07:17


```

