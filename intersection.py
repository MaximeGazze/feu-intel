from typing import Any, Optional

from time import sleep


class Intersection:
    def __init__(self, traffic_lights: dict[str, Any], car_sensors: dict[str, Any]):
        self.traffic_lights: dict[str, Any] = traffic_lights
        self.car_sensors: dict[str, Any] = car_sensors
        self.traffic_direction: Optional[str] = None
        for key, value in traffic_lights.items():
            if value is None:
                continue
            value.intersection = self
        for key, value in car_sensors.items():
            if value is None:
                continue
            value.intersection = self
            value.direction = key

    def change_traffic_direction(self, direction: str) -> None:
        direction = direction.upper()
        change_speed = 1
        if direction == self.traffic_direction:
            return
        for key, value in self.traffic_lights.items():
            if key in ('N', 'S') and direction == 'X':
                value.yellow()
            elif key in ('W', 'E') and direction == 'Y':
                value.yellow()
        sleep(change_speed)
        for key, value in self.traffic_lights.items():
            if direction == 'X':
                if key in ('N', 'S'):
                    value.red()
                elif key in ('W', 'E'):
                    value.green()
            elif direction == 'Y':
                if key in ('N', 'S'):
                    value.green()
                elif key in ('W', 'E'):
                    value.red()
        self.traffic_direction = direction

    def update(self, subject) -> None:
        print(subject)
        if subject.direction in ('N', 'S'):
            self.change_traffic_direction('Y')
        if subject.direction in ('W', 'E'):
            self.change_traffic_direction('X')


# 4 way intersection configuration
#     Nn
#     |
# Ww--+---Ee    UPPERCASE => TrafficLights
#     |         LOWERCASE => CarSensor
#     Ss
# # # # # # # # # # # # # # # # # # # # # # #

class FourWayIntersection(Intersection):
    def __init__(self, N, W, S, E, n, w, s, e):
        traffic_lights: dict[str, Any] = {'N': N, 'W': W, 'S': S, 'E': E}
        car_sensors: dict[str, Any] = {'N': n, 'W': w, 'S': s, 'E': e}
        Intersection.__init__(self, traffic_lights, car_sensors)


# 3 way intersection configuration
#     N
# Ww--+---Ee
#     |         UPPERCASE => TrafficLights
#     |         LOWERCASE => CarSensor
#     s
# # # # # # # # # # # # # # # # # # # # # # #

class ThreeWayIntersection(Intersection):
    def __init__(self, N, W, E, w, s, e):
        traffic_lights: dict[str, Any] = {'N': N, 'W': W, 'E': E}
        car_sensors: dict[str, Any] = {'W': w, 'S': s, 'E': e}
        Intersection.__init__(self, traffic_lights, car_sensors)
