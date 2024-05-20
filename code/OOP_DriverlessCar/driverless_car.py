from vehicle import Vehicle
from lane_detection import LaneDetect
from obstacle_detection import ObstacleDetect
from emergency_brake import EmergencyBrake
from backend import Backend

class DriverlessCar(Vehicle):
    """
    Class represent a driverless car, 
    inheriting from Vehicle.
    """
    def __init__(self, max_speed=50):
        """Initial maximum speed of driverless car."""
        super().__init__()  # Inital the parent Vehicle class.
        self.max_speed = max_speed
        self.maintain_speed = False  # Maintain speed flag to indicate if the car should maintain speed.
        self.lane_detection = LaneDetect()
        self.obstacle_detection = ObstacleDetect()
        self.emergency_brake = EmergencyBrake()
        self.backend = Backend()

    def move(self):
        """Move forward and handle and obstacle detection"""

        # Increase speed until maximun speed is reached.
        while self.speed < self.max_speed:
            self.speed += 10
            self.backend.update_data(f"Speed increased to {self.speed} km/h")   # Log the action data to backend.

            # Check for land deviation and determain direction to turn based on land position.
            if self.lane_detection.deviation_detect:
                direction = 'left' if self.lane_detection.lane_left < self.lane_detection.lane_right else 'right'
                self.turn(direction)

            # Check for obstacles and slow down if detected.
            if self.obstacle_detection.obstacle_detect:
                self.obstacle_detection.slow(self)

                # Apply emergency brake if obstacle is too close.
                if self.obstacle_detection.distance <= self.obstacle_detection.min_distance:
                    self.brake()
                    self.emergency_brake.activate_emergency_brake()
                    break

        # Maintain the car at maximum speed if no deviations or obstacles are detected.
        self.maintain_speed = True
        self.backend.update_data(f"Maintained max speed: {self.speed} km/h")  # Log the action data to backend.

    def turn(self, direction):
        """Define direction to turn."""
        if direction == 'left':  # Turn left to correct land deviation.
            self.lane_detection.turn_left()
        elif direction == 'right':  # Turn right to correct land deviation.
            self.lane_detection.turn_right()
        self.backend.update_data(f"Turned {direction}")  # Log the action data to backend.

    def brake(self):
        """Apply brake to stop car."""
        self.speed = 0  # Set speed to zero.
        self.backend.update_data("Applied brake")  # Log the action data to backend.
        self.maintain_speed = False

    def slow_down(self):
        """Slow down the car."""
        # Reduce the speed by a fixed value
        if self.speed > 0:
            self.speed -= 10
            self.backend.update_data(f"Speed decreased to {self.speed} km/h")  # Log the action data to backend.

    def __str__(self):
        """Return current speed and maximum speed as a string"""
        return f"DriverlessCar speed: {self.speed} km/h, max speed: {self.max_speed} km/h"