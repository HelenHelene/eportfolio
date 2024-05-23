

```python
# Tutorial Lab Challenge: Inheritance

"""
Create a new class called Teacher that inherits from Adult. Provide additional attributes around teacher type
(such as kindergarten, secondary, or higher education) and BMI risk factor (kindergarten = 1, secondary = 2, and higher ed = 3).
Assign BMI risk factors in the initializer based on the type of teacher that is supplied when creating the object.
"""

class Person:
    count = 0

    """Represents a generic Person."""

    def __init__(self, first, last, weight, height, age, gender):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        self.this_age = age
        self.this_gender = gender
        self.bmi = ''
        Person.count += 1

    @classmethod
    def print_count(cls):
        return cls.count

class Adult(Person):
    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)

        print('BMI number is: ' + str(bmi_tmp))
        
        if bmi_tmp < 18:
            self.bmi = 'Underweight'
        elif 18 <= bmi_tmp < 25:
            self.bmi = 'Normal'
        elif 25 <= bmi_tmp < 30:
            self.bmi = 'Overweight'
        elif bmi_tmp >= 30:
            self.bmi = 'Obese'
        return self.bmi

class Child(Person):
    def get_male_bmi(self, age, bmi_temp):
        bmi_class = ''
        if 2 < self.this_age < 9:
            if bmi_temp < 14:
                bmi_class = 'Underweight'
            elif 14 <= bmi_temp < 17:
                bmi_class = 'Normal'
            elif 17 <= bmi_temp < 20:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'
        elif 9 < self.this_age < 16:
            if bmi_temp < 17:
                bmi_class = 'Underweight'
            elif 17 <= bmi_temp < 23:
                bmi_class = 'Normal'
            elif 23 <= bmi_temp < 25:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'
        elif self.this_age >= 16:
            if bmi_temp < 19:
                bmi_class = 'Underweight'
            elif 19 <= bmi_temp < 23:
                bmi_class = 'Normal'
            elif 23 <= bmi_temp < 25:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'
        return bmi_class

    def get_female_bmi(self, age, bmi_temp):
        bmi_class = ''
        if 2 < self.this_age < 9:
            if bmi_temp < 14:
                bmi_class = 'Underweight'
            elif 14 <= bmi_temp < 17:
                bmi_class = 'Normal'
            elif 17 <= bmi_temp < 20:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'
        elif 9 < self.this_age < 16:
            if bmi_temp < 17:
                bmi_class = 'Underweight'
            elif 17 <= bmi_temp < 23:
                bmi_class = 'Normal'
            elif 23 <= bmi_temp < 25:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'
        elif self.this_age >= 16:
            if bmi_temp < 19:
                bmi_class = 'Underweight'
            elif 19 <= bmi_temp < 23:
                bmi_class = 'Normal'
            elif 23 <= bmi_temp < 25:
                bmi_class = 'Overweight'
            else:
                bmi_class = 'Obese'
        return bmi_class
    
    def calc_bmi(self):
        bmi_tmp = (self.weight_in_lbs * 703) / (self.height_in_inches ** 2)
        if self.this_gender == 'M':
            self.bmi = self.get_male_bmi(self.this_age, bmi_tmp)
        elif self.this_gender == 'F':
            self.bmi = self.get_female_bmi(self.this_age, bmi_tmp)
        return self.bmi

class Teacher(Adult):
    def __init__(self, first, last, weight, height, age, gender, teacher_type):
        super().__init__(first, last, weight, height, age, gender)
        self.teacher_type = teacher_type
        self.bmi_risk_factor = self.assign_bmi_risk_factor()

    def assign_bmi_risk_factor(self):
        teacher_types = {
            'kindergarten': 1,
            'secondary': 2,
            'higher_ed': 3
        }
        return teacher_types.get(self.teacher_type, 0)

a1 = Adult('Tom', 'Thumb', 150, 62, 45, 'M')
c1 = Child('Mark', 'Smith', 150, 62, 10, 'M')
t1 = Teacher('Jane', 'Doe', 140, 65, 35, 'F', 'higher_ed')

print(a1.first_name)  # Output: Tom
print(a1.calc_bmi())  # Output: BMI number and category for an adult

print(c1.first_name)  # Output: Mark
print(c1.calc_bmi())  # Output: BMI category for a child

print(t1.first_name)  # Output: Jane
print(t1.calc_bmi())  # Output: BMI number and category for an adult (since Teacher inherits from Adult)
print(t1.teacher_type)  # Output: higher_ed
print(t1.bmi_risk_factor)  # Output: 3
```

```python
# Output
 
Tom
BMI number is: 27.43236212278876
Overweight
Mark
Obese
Jane
BMI number is: 23.294674556213018
Normal
higher_ed
3
```


---

[Return to Module 2 Unit 5](OOP_Unit05.md)
