

```python
# Challenge One

class Person:
    """Represents a generic Person."""
    # CDC range from CDC website
    CDC_under = 18.5
    CDC_good = 24.9

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height

    def calc_bmi(self):
        return (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)

    """Add an instance method called print_self() that, when called, will output the instance object's first name, 
    last name, weight, height, and BMI."""
    def print_self(self):
        bmi = self.calc_bmi()
        print("Name:", self.first_name, self.last_name)
        print("Weight:", self.weight_in_lbs, "lbs")
        print("Height:", self.height_in_inches, "inches")
        print("BMI:", bmi)
    
    """Create another method in your Person class that returns 
    a value indicating if the person is underweight, good weight, or overweight"""
    def get_weight_status(self):
        bmi = self.calc_bmi()
        if bmi < Person.CDC_under:
            return "Underweight"
        elif bmi <= Person.CDC_good:
            return "Good weight"
        else:
            return "Overweight"


# Testing the updated functionality
p1 = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

p1.print_self()
print("Weight status:", p1.get_weight_status())
print("\n")

p2.print_self()
print("Weight status:", p2.get_weight_status())
print("\n")

```

    Name: Tom Thumb
    Weight: 150 lbs
    Height: 62 inches
    BMI: 27.43236212278876
    Weight status: Overweight
    
    
    Name: Fred Flint
    Weight: 225 lbs
    Height: 57 inches
    BMI: 48.68421052631579
    Weight status: Overweight
    
    



```python

```
