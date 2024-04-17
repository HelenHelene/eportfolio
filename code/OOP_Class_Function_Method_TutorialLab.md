

```python
# Tutorial Lab 1: Instance Methods
class Person:
    """Represents a generic Person."""
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

p = Person('Tom', 'Thumb', 150, 62)

print(p.calc_bmi()) 
print("\n")


# Tutorial Lab 2: Demonstrating Instance Methods
p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

print(p.calc_bmi())
print(p2.calc_bmi())
print("\n")


# Tutorial Lab 3: Static Members
class Person:
    count = 0
    
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

print(p.calc_bmi())
print(p2.calc_bmi())
print(Person.count)
print("\n")


# Tutorial Lab 4: Static Methods
class Person:
    count = 0
    
    """Represents a generic Person."""
    
    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)

    @classmethod
    def print_count(cls):
        return cls.count

print(Person.print_count())
```

    27.43236212278876
    
    
    27.43236212278876
    48.68421052631579
    
    
    27.43236212278876
    48.68421052631579
    2
    
    
    0



```python

```
