class ObstacleDetect:
    """Class for handling obstacle detection."""
    
    def __init__(self):
        """Initialize the obstacle detection system."""
        self.obstacle_detect = False
        self.distance = float('inf')
        self.min_distance = 5.0

    def slow(self, car):
        """Slow down the car due to obstacle."""
        print("Slowing down due to obstacle detected")
        car.slow_down()
        self.obstacle_detect = False  # Reset obstacle detection flag after slowing down.

    def update_data(self, distance):
        """Update the obstacle detection data."""
        self.distance = distance
        self.obstacle_detect = distance <= self.min_distance  # Detect obstacle if the distance is <= to the minimum distance.