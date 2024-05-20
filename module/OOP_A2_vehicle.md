```python

class Vehicle:
    """Base class for all vehicles."""

    def __init__(self, speed=0):
        """Initial speed of vehicles."""
        self.speed = speed

    def start(self):
        """Start vehicle engine."""
        print("Engine started")
        self.speed = 0

    def stop(self):
        """Stop vehicle engine."""
        print("Engine stopped")
        self.speed = 0

    def __str__(self):
        """Return vehicle current speed as string"""
        return f"Vehicle speed: {self.speed} km/h"
		
```

---

[Return to Module List](OOP_Assignment2_Scripts.md)
