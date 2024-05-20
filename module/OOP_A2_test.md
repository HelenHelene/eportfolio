```python

from driverless_car import DriverlessCar
from lane_detection import LaneDetect
from obstacle_detection import ObstacleDetect
from emergency_brake import EmergencyBrake
from backend import Backend
from frontend import Frontend

def test_driverless_car():
    """Test the driverless car system."""

    # Initialize components.
    car = DriverlessCar()
    lane_detector = car.lane_detection
    obstacle_detector = car.obstacle_detection
    emergency_brake = car.emergency_brake
    backend = car.backend
    frontend = Frontend(backend)

    # Start car engine.
    car.start()
    assert car.speed == 0  # Ensure the speed is zero after starting the engine.
    car.backend.update_data("Engine started")

    # Move car forward.
    car.move()
    assert car.speed == car.max_speed  # Ensure the car reaches maximum speed.
    car.backend.update_data("Car moved")

    # Simulate lane deviation and correction.
    lane_detector.update_data(2, 1, 1)  # Deviation to the right.
    assert lane_detector.deviation_detect  # Ensure deviation is detected.
    car.turn('left')
    assert not lane_detector.deviation_detect  # Ensure deviation is corrected.

    # Simulate obstacle detection and slowing down.
    obstacle_detector.update_data(10)  # Obstacle detected within safe distance.
    car.obstacle_detection.slow(car)
    car.backend.update_data("Car slowed down due to obstacle")
    
    # Check if the car has slowed down.
    assert car.speed < car.max_speed  # Ensure the car has slowed down.

    # Simulate obstacle detection and emergency brake.
    obstacle_detector.update_data(4)  # Obstacle detected reached minimum distance.
    car.obstacle_detection.slow(car)
    car.brake()
    car.emergency_brake.activate_emergency_brake()
    assert car.speed == 0  # Ensure the car has stopped.
    assert car.emergency_brake.emergency_brake  # Ensure the emergency brake is activated.

    # Stop car engine.
    car.stop()
    assert car.speed == 0  # Ensure speed is zero after stopping the engine.
    car.backend.update_data("Engine stopped")

    # View history.
    frontend.get_data()

# Run the test.
if __name__ == "__main__":
    test_driverless_car()
    print("All tests passed.")
	
```

---

[Return to Module List](OOP_Assignment2_Scripts.md)
