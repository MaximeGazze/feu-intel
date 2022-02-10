from trafficLight import TrafficLight
from carSensor import CarSensor

class Intersection:
    def __init__(self, A = None, B = None, C = None, D = None, a = None, b = None, c = None, d = None):
        self.traffic_light_A = A
        self.traffic_light_B = B
        self.traffic_light_C = C
        self.traffic_light_D = D
        self.car_sensor_a = a
        self.car_sensor_b = b
        self.car_sensor_c = c
        self.car_sensor_d = d
        if self.traffic_light_A: self.traffic_light_A.intersection = self
        if self.traffic_light_B: self.traffic_light_B.intersection = self
        if self.traffic_light_C: self.traffic_light_C.intersection = self
        if self.traffic_light_D: self.traffic_light_D.intersection = self
        if self.car_sensor_a: self.car_sensor_a.intersection = self
        if self.car_sensor_b: self.car_sensor_b.intersection = self
        if self.car_sensor_c: self.car_sensor_c.intersection = self
        if self.car_sensor_d: self.car_sensor_d.intersection = self

    def __str__(self):
        return "asdasd"


# Lettre maj => disposition du senseur, min => disposition du feu de circ.
#     Ac
#     |         configuration a 4 branches
# Bd--+---Db
#     |
#     Ca

# Lettre maj => disposition du senseur, min => disposition du feu de circ.
#     b
# Ac--+---Ca    configuration a 3 branches
#     |
#     |
#     B

