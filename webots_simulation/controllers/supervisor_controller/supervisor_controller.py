"""RN_controller controller."""
import random as rand
from controller import Supervisor, Node
import sys, os
import time
from data import Data
start_time = int(round(time.time() * 1000))

TIME_STEP = 5
DATA_COLLECTION_TIME_SEG = 30
DATA_COLLECTION_TIME_STEP = DATA_COLLECTION_TIME_SEG*1000/TIME_STEP
COLLECTION_NUMBER = 5 #3000
NAME_FILE = "../movement_controller/stop_controller.txt"

TIME_UPDATE_POSE = 200

supervisor = Supervisor()
data_save = Data("pose_real", size_sample=4)

# Numero de casas para formatacao
# decimal_places = 6
# def format_digits(x, y, z, a):
#     return round(x, decimal_places), round(y, decimal_places), round(z, decimal_places), round(a, decimal_places)

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
        print("Trajetorias concluidas: " + str(round(100*(id)/COLLECTION_NUMBER,2)) + "%")
        current_time_step = 0
        current_step_sensor = 0
        while supervisor.step(TIME_STEP) != -1:
            current_time_step += 1
            current_step_sensor += 1

            if (current_time_step > DATA_COLLECTION_TIME_STEP):
                data_save.save()
                start_world_from_zero(robot_node)
                break

            if (current_step_sensor >= (TIME_UPDATE_POSE / TIME_STEP)):
                current_step_sensor = 0
                # print(str(current_time_step*TIME_STEP), "ms")
                robot_node = supervisor.getFromDef("Atlas")
                origin_node = supervisor.getFromDef("origem")
                position = robot_node.getPosition()
                orientation = robot_node.getField("rotation").getSFRotation()[3] # Vx, Vy, Vz, angulo

                sample = position
                sample.append(orientation)
                # sample = format_digits(sample[0], sample[1], sample[2], sample[3])

                # print("Amostra [x,y,z,a]: ", sample)
                data_save.update(sample)

    print("Trajetorias concluidas: 100%")
    open(NAME_FILE, mode='a').close()
    print("\n\n>>>> Tempo de simulacao: ", str(millis()), " segundos")
    # supervisor.simulationQuit(EXIT_SUCCESS)
    supervisor.simulationQuit(0)
