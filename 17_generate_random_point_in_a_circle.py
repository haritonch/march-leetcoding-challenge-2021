from random import uniform
from math import pi, sin, cos, sqrt

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.x_center = x_center
        self.y_center = y_center
        self.radius = radius
        
    def randPoint(self) -> List[float]:
        theta = uniform(0, 2 * pi)
        r = self.radius * sqrt(uniform(0, 1))
        return (self.x_center + r * cos(theta), self.y_center + r * sin(theta))
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()