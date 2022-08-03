"""RN_controller controller."""
import random as rand
from controller import Supervisor, Node
import sys, os
import time
start_time = int(round(time.time() * 1000))

TIME_STEP = 5
DATA_COLLECTION_TIME_SEG = 5
DATA_COLLECTION_TIME_STEP = DATA_COLLECTION_TIME_SEG*1000/TIME_STEP
COLLECTION_NUMBER = 3 #3000
NAME_FILE = "../movement_controller/stop_controller.txt"

supervisor = Supervisor()

def millis():
    return int(round(time.time() * 1000)) - start_time

def start_world_from_zero(atlas_robot):
    # print("Iniciando a simulacao...")
    supervisor.simulationReset()
    atlas_robot.restartController()
    # print("Simulacao resetada")

if os.path.exists(NAME_FILE):
    os.remove(NAME_FILE)

robot_node = supervisor.getFromDef("Atlas")

robot_node.getField("rotation").setSFRotation([0.06976452663644146, -0.1319270503704006, 0.9888013775292586, 0.649943 + rand.randrange(-100, 100, 1)/100])


# Main loop:
while supervisor.step(TIME_STEP) != -1:
    for id in range(COLLECTION_NUMBER):
        print("Andamento:" + str(round(100*(id+1)/COLLECTION_NUMBER,2)), "%")
        current_time_step = 0
        while supervisor.step(TIME_STEP) != -1:
            current_time_step += 1
            robot_node = supervisor.getFromDef("Atlas")
            origin_node = supervisor.getFromDef("origem")
            position = robot_node.getPosition()
            orientation = robot_node.getOrientation()

            if (current_time_step > DATA_COLLECTION_TIME_STEP):
                start_world_from_zero(robot_node)
                break

    open(NAME_FILE, mode='a').close()
    print("\n\n>>>> Tempo de simulacao: ", str(millis()), " segundos")
    # supervisor.simulationQuit(EXIT_SUCCESS)
    supervisor.simulationQuit(0)
