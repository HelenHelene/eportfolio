```python
# Encapsulation Lab 1

import csv

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._new_coffee = []
        self._old_coffee = self.load_coffee()

    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee

# code for testing your script
test_object = CoffeeJournal("code/encapsulation/test_journal1.csv")
test_object.load_coffee()
print(test_object._old_coffee)

```

```python
# Encapsulation Lab 1 Output

[['Roaster', 'Country', 'Region', 'Stars']]

```

---

```python
# Encapsulation Lab 2

import csv

class CoffeeJournal:
    def __init__(self, file):
        self._file = file
        self._roaster = ""
        self._country = ""
        self._region = ""
        self._stars = ""
        self._old_coffee = self.load_coffee()
        self._new_coffee = []

    def load_coffee(self):
        coffee = []
        with open(self._file) as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                coffee.append(row)
        return coffee

    @property
    def roaster(self):
        return self._roaster

    @roaster.setter
    def roaster(self, new_roaster):
        self._roaster = new_roaster

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, new_country):
        self._country = new_country

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, new_region):
        self._region = new_region

    @property
    def stars(self):
        return self._stars

    @stars.setter
    def stars(self, new_stars):
        self._stars = new_stars

# code for testing your script

test_object = CoffeeJournal("code/encapsulation/test_journal2.csv")
test_object.roaster = "Peace River"
test_object.country = "Rwanda"
test_object.region = "Remera"
test_object.stars = "***"
print(test_object.roaster)   
print(test_object.country)  
print(test_object.region) 
print(test_object.stars) 

```

```python
# Encapsulation Lab 2 Output

Peace River
Rwanda
Remera
***

```

---

```python

# Encapsulation Lab 3
import csv

class CoffeeJournal:
  def __init__(self, file):
    self._file = file
    self._roaster = ""
    self._country = ""
    self._region = ""
    self._stars = ""
    self._old_coffee = self.load_coffee()
    self._new_coffee = []
    
  def load_coffee(self):
    coffee = []
    with open(self._file) as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        coffee.append(row)
    return coffee

  @property
  def roaster(self):
    return self._roaster
  
  @roaster.setter
  def roaster(self, new_roaster):
    self._roaster = new_roaster

  @property
  def country(self):
    return self._country
  
  @country.setter
  def country(self, new_country):
    self._country = new_country
    
  @property
  def region(self):
    return self._region
  
  @region.setter
  def region(self, new_region):
    self._region = new_region
    
  @property
  def stars(self):
    return self._stars
  
  @stars.setter
  def stars(self, new_stars):
    self._stars = new_stars

  def save(self):
    with open(self._file, 'a') as f:
      writer = csv.writer(f)
      writer.writerows(self._new_coffee)
  
  def show_coffee(self):
    print()
    if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
      print("Enter a coffee first")
    elif len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
      for row in self._old_coffee:
        print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
    else:
      for row in self._old_coffee:
        print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
      for row in self._new_coffee:
        print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
    print()
    
  def add_coffee(self):
    self._new_coffee.append([self._roaster, self._country, self._region, self._stars])

# code for testing your script

test_object = CoffeeJournal("code/encapsulation/test_journal3.csv")

# print journal with no coffee information
test_object.show_coffee()

# save information to the CSV file and then print
test_object.roaster = "Peace River"
test_object.country = "Rawanda"
test_object.region = "Remera"
test_object.stars = "***"
test_object.add_coffee()
test_object.save()
test_object = CoffeeJournal("code/encapsulation/test_journal3.csv")
test_object.show_coffee()

# print from both the CSV and from `_new_coffee`
test_object.roaster = "Peace River"
test_object.country = "Ethiopia"
test_object.region = "Sidoma"
test_object.stars = "****"
test_object.add_coffee()
test_object.show_coffee()


```

```python
# Encapsulation Lab 3 Output

Enter a coffee first


Roaster         Country         Region           Stars          
Peace River     Rawanda         Remera           ***            


Roaster         Country         Region           Stars          
Peace River     Rawanda         Remera           ***            
Peace River     Ethiopia        Sidoma           ****

```

--- 

```python
# Encapsulation Lab 4

import csv

class CoffeeJournal:
  def __init__(self, file):
    self._file = file
    self._roaster = ""
    self._country = ""
    self._region = ""
    self._stars = ""
    self._old_coffee = self.load_coffee()
    self._new_coffee = []
    
  def load_coffee(self):
    coffee = []
    with open(self._file) as f:
      reader = csv.reader(f, delimiter=',')
      for row in reader:
        coffee.append(row)
    return coffee
  
  @property
  def roaster(self):
    return self._roaster
  
  @roaster.setter
  def roaster(self, new_roaster):
    self._roaster = new_roaster

  @property
  def country(self):
    return self._country
  
  @country.setter
  def country(self, new_country):
    self._country = new_country
    
  @property
  def region(self):
    return self._region
  
  @region.setter
  def region(self, new_region):
    self._region = new_region
    
  @property
  def stars(self):
    return self._stars
  
  @stars.setter
  def stars(self, new_stars):
    self._stars = new_stars

  def save(self):
    with open(self._file, 'a') as f:
      writer = csv.writer(f)
      writer.writerows(self._new_coffee)
  
  def show_coffee(self):
    print()
    if len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
      print("Enter a coffee first")
    elif len(self._old_coffee) < 2 and len(self._new_coffee) == 0:
      for row in self._old_coffee:
        print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
    else:
      for row in self._old_coffee:
        print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
      for row in self._new_coffee:
        print(f"{row[0]:15} {row[1]:15} {row[2]:15}  {row[3]:15}")
    print()
    
  def add_coffee(self):
    self._new_coffee.append([self._roaster, self._country, self._region, self._stars])
  
def main_menu():
  print("Coffess of the World")
  print("\t1. Show Coffee")
  print("\t2. Add Coffee")
  print("\t3. Save and Quit")
  choice = int(input("Enter the number of your selection: "))
  return choice
  
def perform_action(choice, coffee):
  if choice == 1:
    coffee.show_coffee()
  elif choice == 2:
    enter_coffee(coffee)
  elif choice == 3:
    quit(coffee)
  
def enter_coffee(coffee):
  print()
  coffee.roaster = input("Enter the name of the roaster: ")
  coffee.country = input("Enter the country of origin: ")
  coffee.region = input("Enter the region: ")
  coffee.stars = input("Enter the number of stars '*' (1-4): ")
  print()
  coffee.add_coffee()
  
def quit(coffee):
  global run_loop
  coffee.save()
  run_loop = False
  
# code for testing your script

run_loop = True
file = "code/encapsulation/coffee_journal.csv"
my_coffee = CoffeeJournal(file)

while run_loop:
  choice = main_menu()
  perform_action(choice, my_coffee)
```


```python
# Encapsulation Lab 4 Output

Coffess of the World
        1. Show Coffee
        2. Add Coffee
        3. Save and Quit
Enter the number of your selection: 2

Enter the name of the roaster: Ritual
Enter the country of origin: Guatemala
Enter the region: Antigua
Enter the number of stars '*' (1-4): 3

Coffess of the World
        1. Show Coffee
        2. Add Coffee
        3. Save and Quit
Enter the number of your selection: 1

Roaster         Country         Region           Stars          
Peace River     Rawanda         Remera           ***            
Ritual          Guatemala       Antigua          3              

Coffess of the World
        1. Show Coffee
        2. Add Coffee
        3. Save and Quit

```

---

```python
# Encapsulation Lab Challenge

class Person:
    def __init__(self, name, age, occupation):
        self._name = name
        self._age = age
        self._occupation = occupation

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        self._name = new_name

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        self._age = new_age

    def get_occupation(self):
        return self._occupation

    def set_occupation(self, new_occupation):
        self._occupation = new_occupation

# Example usage:
my_person = Person("Citra Curie", 16, "student")
print(my_person.get_name())         
my_person.set_name("Rowan Faraday")
print(my_person.get_name())         

print(my_person.get_age())          
my_person.set_age(18)
print(my_person.get_age())          

print(my_person.get_occupation())   
my_person.set_occupation("plumber")
print(my_person.get_occupation())

```

```python
# Encapsulation Lab Challenge Output

Citra Curie
Rowan Faraday
16
18
student
plumber

```

---

[Return to Module 2 Unit 6](OOP_Unit06.md)
