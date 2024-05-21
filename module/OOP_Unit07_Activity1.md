### Discuss the ways in which data structures support object-oriented development with examples of three different data structures

Data structures are fundamental to object-oriented development as they provide efficient ways to organize, manage, and store data within a program. 
Here are three examples of different data structures and how they support object-oriented development:

### Lists:
Lists allow for dynamic collections of objects. Methods can iterate over these lists to perform operations on each car, such as displaying details or calculating total mileage.

Example: Consider a Car class that keeps track of multiple car objects.

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

cars = []
cars.append(Car('Toyota', 'Corolla', 2018))
cars.append(Car('Ford', 'Mustang', 2020))

for car in cars:
    print(car.make, car.model, car.year)
```

### Dictionaries:
Dictionaries allow for quick lookups, additions, and deletions of objects using keys. This is useful for managing objects with unique identifiers.

Example: A Garage class that keeps track of cars using their license plates as keys.

```python
class Car:
    def __init__(self, license_plate, make, model):
        self.license_plate = license_plate
        self.make = make
        self.model = model

garage = {}
garage['ABC123'] = Car('ABC123', 'Tesla', 'Model S')
garage['XYZ789'] = Car('XYZ789', 'BMW', 'i8')

for plate, car in garage.items():
    print(plate, car.make, car.model)
```

### Queues:
Queues are important for operations that require processing in a first-in, first-out (FIFO) manner. 
This is critical for managing tasks such as service requests.

Example: A ServiceQueue class to manage cars waiting for service.

```python
from collections import deque

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

service_queue = deque()
service_queue.append(Car('Honda', 'Civic'))
service_queue.append(Car('Audi', 'A4'))

while service_queue:
    car = service_queue.popleft()
    print(f'Servicing {car.make} {car.model}')
```

---

[Return to Module 2 Unit 7](OOP_Unit07.md)
