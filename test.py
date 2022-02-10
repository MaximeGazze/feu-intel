from intersection import Intersection
from trafficLight import TrafficLight
from carSensor import CarSensor
from time import sleep

# tl: TrafficLight = TrafficLight(18, 12, 16)
# tl.red()
# sleep(1)
# tl.off()

# intersection = Intersection(
#     TrafficLight(18, 12, 16),
#     TrafficLight(18, 12, 16),
#     TrafficLight(18, 12, 16),
#     TrafficLight(18, 12, 16),
#     CarSensor(23, 24),
#     CarSensor(23, 24),
#     CarSensor(20, 21),
#     CarSensor(20, 21),
# )


# intersection = Intersection(
#     TrafficLight(18, 12, 16),
#     None,
#     None,
#     None,
#     CarSensor(23, 24),
#     CarSensor(20, 21),
#     # None,
#     None,
#     None,
# )

# print(intersection.car_sensor_a.distance)

# while True:
#     print('distance', intersection.car_sensor_a.distance)
#     sleep(1)

c = CarSensor(23, 24)
sleep(1)
print(c.distance)


# intersection.traffic_light_A.red()
# sleep(2)
# intersection.traffic_light_A.off()

# intersection = Intersection(
#     TrafficLight(18, 12, 16),
#     TrafficLight(21, 22, 23),
#     TrafficLight(21, 22, 23),
#     TrafficLight(21, 22, 23),
#     CarSensor(21, 24),
#     CarSensor(21, 24),
#     CarSensor(21, 24),
#     CarSensor(21, 24),
# )

# print(intersection)
# print(intersection.traffic_light_A)
# intersection.traffic_light_A.red()

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def namea(self):
#         print(self.name)

# p1 = Person('john')
# p1.namea()
