

```python
# Session 17.3 

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    # converts Times to integers:
    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    # converts an integer to a Time
    # static method, indicated by using the @staticmethod decorator. 
    @staticmethod  
    def int_to_time(seconds):
        time = Time(0, 0, 0) # Create a new Time object
        minutes, time.second = divmod(seconds, 60)
        time.hour, time.minute = divmod(minutes, 60)
        return time

    #Increment method inside class
    def increment(self, seconds):
        seconds += self.time_to_int()
        return Time.int_to_time(seconds)  # Use the class name to call the static method
    
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

# Create Time object
start = Time(9, 45, 0)
end = start.increment(1337)

# Print Incremented Time object
end.print_time()

```

```python

# Output
    10:07:17

```
