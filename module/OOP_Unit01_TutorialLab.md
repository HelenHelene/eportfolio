

```python
# Tutorial Lab 1:Creating a Class
class Person:
    #Represents a generic Person.
    def __init__(self, first, last, weight, height):
      self.first_name = first
      self.last_name = last
      self.weight_in_lbs = weight
      self.height_in_inches = height

print(Person)

# Tutorial Lab 2: Instantiate a Class
p = Person('Tom', 'Thumb', 150, 78)
print(p.first_name + ' ' + p.last_name + ' weighs ' + str(p.weight_in_lbs) + 'lbs.')

# Tutorial Lab 3: Modify Instance Data Members
p.first_name = 'George'
print(p.first_name + ' ' + p.last_name + ' weighs ' + str(p.weight_in_lbs) + 'lbs.')

# Tutorial Lab Challenge
# Create five Person objects
p1 = Person("Tom", "Thumb", 150, 78)
p2 = Person("Fred", "Frainer", 155, 80)
p3 = Person("George", "Ganahl", 165, 85)
p4 = Person("Tanya", "Taylor", 170, 90)
p5 = Person("Mary", "Marent", 175, 95)

# Create a list and store the Person objects in it
person_list = [p1, p2, p3, p4, p5]

# Iterate over the list and print the first names
for person in person_list:
    print(person.first_name)
```

```python
# Output
    <class '__main__.Person'>
    Tom Thumb weighs 150lbs.
    George Thumb weighs 150lbs.
    Tom
    Fred
    George
    Tanya
    Mary

```


---

[Return to Module 2 Unit 1](OOP_Unit01.md)
