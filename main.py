from intersection import FourWayIntersection
from trafficLight import TrafficLight
from carSensor import CarSensor
from time import sleep

from aliot.aliot import alive_iot as iot

# Url pour se connecter au services du site
iot.ObjConnecteAlive.set_url("wss://albumfamilial.ca/iotgateway/")
iot.ObjConnecteAlive.set_api_url("https://albumfamilial.ca/api")

# Id de votre objet connecté
my_iot = iot.ObjConnecteAlive(
	object_id="d8c5fee2-fb62-4f62-ae8b-3990126473b9"
)

intersection = FourWayIntersection(
    TrafficLight(5, 6, 16),   #N
    TrafficLight(13, 19, 26), #W
    TrafficLight(8, 7, 10),   #S
    TrafficLight(17, 27, 22), #E
    CarSensor(20, 21),  # n
    CarSensor(25, 24),  # w 
    CarSensor(18, 4),   # s
    CarSensor(23, 12),  # e
)

@my_iot.main_loop()
def main():
    states = intersection.returnStates();
    my_iot.update_doc({
        "/document/lights/W/state": states["W"].lightsStates(),
        "/document/lights/E/state": states["E"].lightsStates(),
        "/document/lights/S/state": states["S"].lightsStates(),
        "/document/lights/N/state": states["N"].lightsStates(),
        })
    print("\n W: {} \n E: {} \n S: {} \n N: {}".format(states["W"].lightsStates(), states["E"].lightsStates(), states["S"].lightsStates(), states["N"].lightsStates()))
    print(states)
    sleep(1)
my_iot.begin()

