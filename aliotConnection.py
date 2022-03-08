from aliot.aliot import alive_iot as iot

projectId = '50cd307b-a3d6-45a1-9664-b4178a96009c'
my_iot = iot.ObjConnecteAlive(object_id="0cc3f29e-422c-44d0-8f0c-62a8854f58bd")


def change_traffic_light_state(traffic_light):
    my_iot.send_update(projectId, traffic_light.identifier, traffic_light.state)

@my_iot.main_loop()
def main():
    my_iot.send_update(projectId, 'traffic_light', True)
    # my_iot.send_update(projectId, traffic_light.identifier, traffic_light.state)


my_iot.begin()
