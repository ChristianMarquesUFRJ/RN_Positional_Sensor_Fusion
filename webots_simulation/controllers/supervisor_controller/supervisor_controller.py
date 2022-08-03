"""RN_controller controller."""
import random as rand
from controller import Supervisor, Node
import sys, os
import time
start_time = int(round(time.time() * 1000))
# from sensors.encoder import Encoder
# from sensors.gps import _GPS
# from sensors.mpu import MPU

TIME_STEP = 5
DATA_COLLECTION_TIME_SEG = 2#30
COLLECTION_NUMBER = 2 #3000
NAME_FILE = "../movement_controller/stop_controller.txt"

supervisor = Supervisor()

# Criação dos Sensores
# left_encoder = Encoder("left_rear_sensor",TIME_STEP)
# right_encoder = Encoder("right_rear_sensor",TIME_STEP)
# gps1 = _GPS("gps_real_1",TIME_STEP)
# gps2 = _GPS("gps_real_2",TIME_STEP)
# mpu1 = MPU(1,TIME_STEP)
# mpu2 = MPU(2,TIME_STEP)

def millis():
    return int(round(time.time() * 1000)) - start_time

def start_world_from_zero(atlas_robot):
    print("Iniciando a simulacao...")
    supervisor.simulationReset()
    atlas_robot.restartController()
    print("Simulacao resetada")

if os.path.exists(NAME_FILE):
    os.remove(NAME_FILE)

robot_node = supervisor.getFromDef("Atlas")

robot_node.getField("rotation").setSFRotation([0.06976452663644146, -0.1319270503704006, 0.9888013775292586, 0.649943 + rand.randrange(-100, 100, 1)/100])


# Main loop:
while supervisor.step(TIME_STEP) != -1:
    for id in range(COLLECTION_NUMBER):
        print("Nº " + str(id+1))
        current_time_step = 0
        while supervisor.step(TIME_STEP) != -1:
            current_time_step += 1
            robot_node = supervisor.getFromDef("Atlas")
            origin_node = supervisor.getFromDef("origem")
            position = robot_node.getPosition()
            orientation = robot_node.getOrientation()

            sim_time = supervisor.getTime()

            if (sim_time >= DATA_COLLECTION_TIME_SEG):
                start_world_from_zero(robot_node)
                break

            # if(current_time_step % 200 == 0):
            #     current_time_step = 0

            # Obtencao dos valores dos sensores
            # wheel_ticks_values = left_encoder.get_ticks(), right_encoder.get_ticks()
            # accel1_values, gyro1_values, mag1_values = mpu1.get_accel(), mpu1.get_gyro(), mpu1.get_mag()
            # accel2_values, gyro2_values, mag2_values = mpu2.get_accel(), mpu2.get_gyro(), mpu2.get_mag()
            # gps1_values = gps1.get_value()
            # gps2_values = gps2.get_value() 

            # pose = robot_node.getPose()
            # print("Supervisor: Tempo simulacao =" + str(sim_time) + " || Tempo PC = " + str(millis()/1000))
            # print("Encoder" + str(wheel_ticks_values))
            print("Supervisor - orientation: " + str(orientation) + "\n")
            # print(sim_time)

    print("\n>>>> ACABOU A PAÇOCA")
    open(NAME_FILE, mode='a').close()
    start_time = supervisor.getTime()
    # supervisor.simulationQuit(0)
    supervisor.simulationQuit(EXIT_SUCCESS)
