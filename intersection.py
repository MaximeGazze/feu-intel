from trafficLight import TrafficLight
from carSensor import CarSensor
from time import sleep

class Intersection:
# 4 way intersection configuration
#     Nn
#     |
# Ww--+---Ee    UPPERCASE => TrafficLights
#     |         LOWERCASE => CarSensor
#     Ss
# # # # # # # # # # # # # # # # # # # # # # #
    def __init__(self, N, W, S, E, n, w, s, e):
        self.traffic_lights = {'N': N, 'W': W, 'S': S, 'E': E}
        self.car_sensors = {'N': n, 'W': w, 'S': s, 'E': e}
        self.traffic_direction = None
        for key, value in self.traffic_lights.items():
            if (value == None): continue
            value.intersection = self
        for key, value in self.car_sensors.items():
            if (value == None): continue
            value.intersection = self
            value.direction = key

    def change_traffic_direction(self, direction: str) -> None:
        direction = direction.upper()
        change_speed = 1
        if (direction == self.traffic_direction): return
        for key, value in self.traffic_lights.items():
            if (key in ('N', 'S') and direction == 'X'):
                value.yellow()
            elif (key in ('W', 'E') and direction == 'Y'):
                value.yellow()
        sleep(change_speed)
        for key, value in self.traffic_lights.items():
            if (direction == 'X'):
                if (key in ('N', 'S')):
                    value.red()
                elif (key in ('W', 'E')):
                    value.green()
            elif (direction == 'Y'):
                if (key in ('N', 'S')):
                    value.green()
                elif (key in ('W', 'E')):
                    value.red()
        self.traffic_direction = direction

    def update(self, subject):
        print(subject)
        if (subject.direction in ('N', 'S')): self.change_traffic_direction('Y')
        if (subject.direction in ('W', 'E')): self.change_traffic_direction('X')


# Lettre maj => disposition du senseur, min => disposition du feu de circ.
#     N
# Ww--+---Ee    configuration a 3 branches
#     |
#     |
#     s

