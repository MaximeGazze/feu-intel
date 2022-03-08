from intersection import FourWayIntersection
from trafficLight import TrafficLight
from carSensor import CarSensor
from time import sleep

from aliot.aliot import alive_iot as iot

# Id du projet à modifier
projectId = '03abafda-6f0f-4747-a0e2-1d50f73995f3'

# Url pour se connecter au services du site
iot.ObjConnecteAlive.set_url("wss://alivecode.ca/iotgateway/")

# Id de votre objet connecté
my_iot = iot.ObjConnecteAlive(
	object_id="bee228d1-8dc7-4bb5-91c0-b7e0d111cb8d"
)

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

@my_iot.main_loop()
def main():
    states = intersection.returnStates();
    my_iot.update(projectId, {
        "/documents/lights/W/state": states["W"].lightsStates(),
        "/documents/lights/E/state": states["E"].lightsStates(),
        "/documents/lights/S/state": states["S"].lightsStates(),
        "/documents/lights/N/state": states["N"].lightsStates(),
        })
    sleep(1)
my_iot.begin()
