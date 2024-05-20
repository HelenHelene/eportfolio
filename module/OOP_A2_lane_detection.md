
```python

class LaneDetect:
    """Class for handling land detection."""

    def __init__(self):
        """Initial the land dection system."""
        self.lane_left = 0.0
        self.lane_right = 0.0
        self.deviation = 0.0
        self.deviation_detect = False

    def turn_left(self):
        """Correct car position by turning left."""
        self.deviation_detect = False
        print("Turning left to correct lane")

    def turn_right(self):
        """Correct car position by turning right."""
        self.deviation_detect = False
        print("Turning right to correct lane")

    def update_data(self, lane_left, lane_right, deviation):
        """Update lane detection data."""
        self.lane_left = lane_left  # Distance to the left lane marker.
        self.lane_right = lane_right  # Distance to right lane marker.
        self.deviation = deviation  # Deviation from the center of the lane.
        self.deviation_detect = deviation > 0  # Detect deviation if deviation value > 0.
		
```