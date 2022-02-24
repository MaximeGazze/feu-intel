from intersection import FourWayIntersection
from trafficLight import TrafficLight
from carSensor import CarSensor
from time import sleep

intersection = FourWayIntersection(
    TrafficLight(13, 19, 26),
    TrafficLight(5, 6, 16),
    TrafficLight(17, 27, 22),
    TrafficLight(23, 24, 25),
    None, # N 8 12
    None, # W 7 10
    CarSensor(18, 4), # S
    CarSensor(20, 21), # E
)

while True:
    try:
        sleep(0.1)
    except KeyboardInterrupt:
        break
