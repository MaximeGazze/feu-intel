from intersection import FourWayIntersection
from trafficLight import TrafficLight
from carSensor import CarSensor
from time import sleep

from aliot.aliot import alive_iot as iot

# Id du projet à modifier
#projectId = '03abafda-6f0f-4747-a0e2-1d50f73995f3'

# Url pour se connecter au services du site
iot.ObjConnecteAlive.set_url("ws://albumfamilial.ca:8881/")

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
#TODO a effacer la boucle
#while True:
def main():
    states = intersection.returnStates();
    my_iot.update_doc({
        "/documents/lights/W/state": states["W"].lightsStates(),
        "/documents/lights/E/state": states["E"].lightsStates(),
        "/documents/lights/S/state": states["S"].lightsStates(),
        "/documents/lights/N/state": states["N"].lightsStates(),
        })
    print("\n W: {} \n E: {} \n S: {} \n N: {}".format(states["W"].lightsStates(), states["E"].lightsStates(), states["S"].lightsStates(), states["N"].lightsStates()))
    print(states)
    sleep(1)
my_iot.begin()

