```python
# Encapsulation Ex. 1
"""Define the Country class which has attributes for name, capital, population, and continent.
Please use the Python convention for making these attributes private."""

class Country:
    def __init__(self, name, capital, population, continent):
        # Using single underscore to indicate protected attributes
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent

# Initialize an object of the Country class
my_country = Country('France', 'Paris', 67081000, 'Europe')

# Print the attributes using single leading underscore
print(my_country._name)  # France
print(my_country._capital)  # Paris
print(my_country._population)  # 67081000
print(my_country._continent)  # Europe

```

```python
# Encapsulation Ex. 1 Output

France
Paris
67081000
Europe
```

---

```python
# Encapsulation Ex. 2
"""Define the Artist class which has attributes for name, medium, style, and famous_artwork.
Do not use the Python convention to make these attributes."""

class Artist:
    def __init__(self, name, medium, style, famous_artwork):
        # Using double underscores to make attributes private
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

# Initialize an object of the Artist class
my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

# Attempt to print the attributes directly (this will raise an error)
try:
    print(my_artist.name)
except AttributeError as e:
    print(f"Error Message: {e}")

try:
    print(my_artist.medium)
except AttributeError as e:
    print(f"Error Message: {e}")

try:
    print(my_artist.style)
except AttributeError as e:
    print(f"Error Message: {e}")

try:
    print(my_artist.famous_artwork)
except AttributeError as e:
    print(f"Error Message: {e}")

# Print the attributes using the name mangling format
print(my_artist._Artist__name)  # Bill Watterson
print(my_artist._Artist__medium)  # ink and paper
print(my_artist._Artist__style)  # cartoons
print(my_artist._Artist__famous_artwork)  # Calvin and Hobbes

```

```python
# Encapsulation Ex. 2 Output

Error Message: 'Artist' object has no attribute 'name'
Error Message: 'Artist' object has no attribute 'medium'
Error Message: 'Artist' object has no attribute 'style'
Error Message: 'Artist' object has no attribute 'famous_artwork'
Bill Watterson
ink and paper
cartoons
Calvin and Hobbes
```

---

```python
# Encapsulation Ex. 3
"""Define the BankAccount class which has attributes for checking and savings.
Use the Python convention to make these attributes private.
Create the getters get_checking and get_savings, and create the setters set_checking and set_savings."""

class BankAccount():
  def __init__(self):
    self._checking = 0
    self._savings = 0
    
  def get_checking(self):
    return self._checking
  
  def set_checking(self, new_value):
    self._checking = new_value
    
  def get_savings(self):
    return self._savings
  
  def set_savings(self, new_value):
    self._savings = new_value

# Example usage:
my_account = BankAccount()
my_account.set_checking(523.48)
print(my_account.get_checking())  # Output: 523.48
my_account.set_savings(386.15)
print(my_account.get_savings())  # Output: 386.15

```

```python
# Encapsulation Ex. 3 Output

523.48
386.15
```

--- 

```python
# Encapsulation Ex. 4
"""Define the Dancer class which has attributes for name, nationality, and style.
Use the Python convention to make these attributes private.
Create the getters and setters using the property function."""

class Dancer:
  def __init__(self, name, nationality, style):
    self._name = name
    self._nationality = nationality
    self._style = style
    
  def get_name(self):
    return self._name
  
  def set_name(self, new_value):
    self._name = new_value
    
  def get_nationality(self):
    return self._nationality
  
  def set_nationality(self, new_value):
    self._nationality = new_value
    
  def get_style(self):
    return self._style
  
  def set_style(self, new_value):
    self._style = new_value
    
  name = property(get_name, set_name)
  nationality = property(get_nationality, set_nationality)
  style = property(get_style, set_style)

# Example usage:
my_dancer = Dancer("Savion Glover", "American", "tap")
print(my_dancer.name)          # Output: Savion Glover
print(my_dancer.nationality)   # Output: American
print(my_dancer.style)         # Output: tap

my_dancer.name = 'Anna Pavlova'
my_dancer.nationality = 'Russian'
my_dancer.style = 'ballet'

print(my_dancer.name)          # Output: Anna Pavlova
print(my_dancer.nationality)   # Output: Russian
print(my_dancer.style)         # Output: ballet

```

```python
# Encapsulation Ex. 4 Output

Savion Glover
American
tap
Anna Pavlova
Russian
ballet
```

---

```python
# Encapsulation Ex. 5
"""Define the Cyclist class which has attributes name, nationality, and nickname.
Use the Python convention to make these attributes private.
Create the getters and setters using the property decorator."""

class Cyclist:
  def __init__(self, name, nationality, nickname):
    self._name = name
    self._nationality = nationality
    self._nickname = nickname
    
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, new_value):
    self._name = new_value
    
  @property
  def nationality(self):
    return self._nationality
  
  @nationality.setter
  def nationality(self, new_value):
    self._nationality = new_value
    
  @property
  def nickname(self):
    return self._nickname
  
  @nickname.setter
  def nickname(self, new_value):
    self._nickname = new_value

# Example usage:
my_cyclist = Cyclist("Greg LeMond", "American", "Le Monstre")
print(my_cyclist.name)          # Output: Greg LeMond
print(my_cyclist.nationality)   # Output: American
print(my_cyclist.nickname)      # Output: Le Monstre

my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"

print(my_cyclist.name)          # Output: Eddy Merckx
print(my_cyclist.nationality)   # Output: Belgian
print(my_cyclist.nickname)      # Output: The Cannibal

```

```python
# Encapsulation Ex. 5 Output

Greg LeMond
American
Le Monstre
Eddy Merckx
Belgian
The Cannibal
```

---

[Return to Module 2 Unit 6](OOP_Unit06.md)
