### Create a nested dictionary of data on cars within a Car class and work with it by calling the methods: items(), keys(), values()

Data structures are fundamental to object-oriented development as they provide efficient ways to organize, manage, and store data within a program. 
Here are three examples of different data structures and how they support object-oriented development:

```python
class Car:
    def __init__(self):
        self.cars = {}

    def add_car(self, make, model, year, specs):
        if make not in self.cars:
            self.cars[make] = {}
        self.cars[make][model] = {'year': year, 'specs': specs}

    def display_items(self):
        return self.cars.items()

    def display_keys(self):
        return self.cars.keys()

    def display_values(self):
        return self.cars.values()

# Create Car instance and add cars
garage = Car()
garage.add_car('Toyota', 'Corolla', 2018, {'color': 'red', 'hp': 132})
garage.add_car('Ford', 'Mustang', 2020, {'color': 'blue', 'hp': 450})

# Display items, keys, and values
print("Items:", garage.display_items())
print("Keys:", garage.display_keys())
print("Values:", garage.display_values())
```

---

[Return to Module 2 Unit 7](OOP_Unit07.md)
