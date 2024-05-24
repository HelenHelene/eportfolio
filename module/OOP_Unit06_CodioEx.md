```python
# Encapsulation Ex. 1

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

```python
# Encapsulation Ex. 2

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

[Return to Module 2 Unit 6](OOP_Unit06.md)
