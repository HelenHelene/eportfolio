

```python
# Exercise 16.1

class Time:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
       
    def __mul__(self, number):
        return self.mul_time(number)

    def mul_time(self, number):
        total_seconds = self.time_to_seconds() * number
        return Time.int_to_time(total_seconds)

    def time_to_seconds(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    @staticmethod
    def int_to_time(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return Time(hours, minutes, seconds)

def calculate_average_pace(finishing_time, distance):
    seconds_per_mile = finishing_time.time_to_seconds() / distance
    minutes_per_mile = seconds_per_mile // 60
    seconds = seconds_per_mile % 60
    return Time(0, minutes_per_mile, seconds)


# Example usage
race_time = Time(3, 34, 5)
marathon_distance = 26.2  # Distance in miles

average_pace = calculate_average_pace(race_time, marathon_distance)
print("Average Pace for a marathon: {:.2f} minutes/mile".format(average_pace.minute + average_pace.second / 60))
```

    Average Pace for a marathon: 8.17 minutes/mile



```python

```
