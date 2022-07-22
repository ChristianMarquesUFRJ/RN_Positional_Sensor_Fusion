"""RN_controller controller."""
from controller import Supervisor, Node

supervisor = Supervisor()

TIME_STEP = 32
DATA_COLLECTION_TIME_SEG = 5
COLLECTION_NUMBER = 2

def start_world_from_zero(atlas_robot):
    print("Iniciando a simulacao...")
    supervisor.simulationReset()
    atlas_robot.restartController()
    print("Simulacao resetada")

# Main loop:
for id in range(COLLECTION_NUMBER):
    print("Nº " + str(id+1))
    while supervisor.step(TIME_STEP) != -1:
        robot_node = supervisor.getFromDef("Atlas")
        origin_node = supervisor.getFromDef("origem")

        position = robot_node.getPosition()
        orientation = robot_node.getOrientation()

        sim_time = supervisor.getTime()

        if (sim_time >= DATA_COLLECTION_TIME_SEG):
            start_world_from_zero(robot_node)
            break

        # pose = robot_node.getPose()
        print("Supervisor: " + str(sim_time) + " - posicao: " + str(position))
        # print("Supervisor - pose: " + str(position) + " | " + str(orientation))
        # print(sim_time)
