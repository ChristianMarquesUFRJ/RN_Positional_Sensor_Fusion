"""RN_controller controller."""
from controller import Supervisor, Node
import sys, os
# from sensors.encoder import Encoder
# from sensors.gps import _GPS
# from sensors.mpu import MPU

TIME_STEP = 32
DATA_COLLECTION_TIME_SEG = 2
COLLECTION_NUMBER = 2 #10000
NAME_FILE = "../movement_controller/stop_controller.txt"

supervisor = Supervisor()

# Criação dos Sensores
# left_encoder = Encoder("left_rear_sensor",TIME_STEP)
# right_encoder = Encoder("right_rear_sensor",TIME_STEP)
# gps1 = _GPS("gps_real_1",TIME_STEP)
# gps2 = _GPS("gps_real_2",TIME_STEP)
# mpu1 = MPU(1,TIME_STEP)
# mpu2 = MPU(2,TIME_STEP)

def start_world_from_zero(atlas_robot):
    print("Iniciando a simulacao...")
    supervisor.simulationReset()
    atlas_robot.restartController()
    print("Simulacao resetada")

if os.path.exists(NAME_FILE):
    os.remove(NAME_FILE)

# Main loop:
while supervisor.step(TIME_STEP) != -1:
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
                
        
            # Obtencao dos valores dos sensores
            # wheel_ticks_values = left_encoder.get_ticks(), right_encoder.get_ticks()
            # accel1_values, gyro1_values, mag1_values = mpu1.get_accel(), mpu1.get_gyro(), mpu1.get_mag()
            # accel2_values, gyro2_values, mag2_values = mpu2.get_accel(), mpu2.get_gyro(), mpu2.get_mag()
            # gps1_values = gps1.get_value()
            # gps2_values = gps2.get_value() 

        
            # Visualizacao no terminal
            # print("Encoder" + str(wheel_ticks_values), end=" | ")
            # print("MPU1[" + str(accel1_values) + "g; " + str(gyro1_values) + "*/s; " + str(mag1_values) + "uT]", end=" | ")
            # # print("MPU2[" + str(accel2_values) + "g; " + str(gyro2_values) + "*/s; " + str(mag2_values) + "uT]", end=" | ")
            # print("GPS1" + str(gps1_values), end=" | ")
            # # print("GPS2" + str(gps2_values), end=" | ")
            # print("")

            # pose = robot_node.getPose()
            print("Supervisor: " + str(sim_time) + " - posicao: " + str(position))
            # print("Encoder" + str(wheel_ticks_values))
            # print("Supervisor - pose: " + str(position) + " | " + str(orientation))
            # print(sim_time)

    print("\n>>>> ACABOU A PAÇOCA")
    open(NAME_FILE, mode='a').close()
    start_time = supervisor.getTime()
    supervisor.simulationQuit(EXIT_SUCCESS)
