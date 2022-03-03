from typing import Any, Optional
from time import sleep


class Intersection:
    def __init__(self, traffic_lights, car_sensors):
        """
        The base intersection class used to create intersections to manage traffic.

        This class is only meant to be inherited from and requires a number of :class:`TrafficLight`
        and :class:`car_sensors` varying with the intersection configuration chosen, or the child
        class eg: :class:`FourWayIntersection` would have 4 traffic lights and car sensors.

        :param traffic_lights: A dictionary containing all the traffic lights associated with the intersection
        :param car_sensors: A dictionary containing all the car sensors associated with the intersection
        """
        self.traffic_lights: dict[str, Any] = traffic_lights
        self.car_sensors: dict[str, Any] = car_sensors
        self.traffic_direction: Optional[str] = None
        for key, value in traffic_lights.items():
            if value is None:
                continue
            value.intersection = self
            value.identifier = 'traffic_light_' + key
        for key, value in car_sensors.items():
            if value is None:
                continue
            value.intersection = self
            value.direction = key

    def change_traffic_direction(self, direction: str) -> None:
        """
        Method used to toggle the traffic of the intersection in the given direction.

        :param direction: Direction to switch to, either 'X' or 'Y'
        :return:
        """
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

    def update(self, notifier) -> None:
        """Method used to update the traffic lights when a car is detected."""
        if notifier.direction in ('N', 'S'):
            self.change_traffic_direction('Y')
        if notifier.direction in ('W', 'E'):
            self.change_traffic_direction('X')
    
    def returnStates(self):
        return self.traffic_lights

# 4 way intersection configuration
#       Nn
#       |
#   Ww--+---Ee    UPPERCASE = > TrafficLights
#       |         LOWERCASE = > CarSensor
#       Ss

class FourWayIntersection(Intersection):
    def __init__(self, N, W, S, E, n, w, s, e):
        """
        Four way intersection configuration used to create an :class:`Intersection` object.

        :param N: North traffic light
        :param W: West traffic light
        :param S: South traffic light
        :param E: East traffic light
        :param n: North car sensor
        :param w: West car sensor
        :param s: South car sensor
        :param e: East car sensor
        """
        traffic_lights: dict[str, Any] = {'N': N, 'W': W, 'S': S, 'E': E}
        car_sensors: dict[str, Any] = {'N': n, 'W': w, 'S': s, 'E': e}
        Intersection.__init__(self, traffic_lights, car_sensors)


# 3 way intersection configuration
#     N
# Ww--+---Ee
#     |         UPPERCASE => TrafficLights
#     |         LOWERCASE => CarSensor
#     s

class ThreeWayIntersection(Intersection):
    def __init__(self, N, W, E, w, s, e):
        r"""
        Four way intersection configuration used to create an :class:`Intersection` object.

        :param N: North traffic light
        :param W: West traffic light
        :param E: East traffic light
        :param w: West car sensor
        :param s: South car sensor
        :param e: East  car sensor
        """
        traffic_lights: dict[str, Any] = {'N': N, 'W': W, 'E': E}
        car_sensors: dict[str, Any] = {'W': w, 'S': s, 'E': e}
        Intersection.__init__(self, traffic_lights, car_sensors)
