#Controlando o Atlas pelo teclado por enquanto

from vehicle import Driver
from movement.autonomous_control import autonomous_control
from sensors.encoder import Encoder
from sensors.gps import _GPS
from sensors.mpu import MPU
import os.path
import sys

driver = Driver()
basicTimeStep = int(driver.getBasicTimeStep())

encoder_update_time_ms = 200
gps_update_time_ms = 1000
imu_update_time_ms = 200
print_update_time_ms = 200

robot_control = autonomous_control(driver)


def convert_time_to_time_step(time):
    return int(time / basicTimeStep)

def convert_time_step_to_time(time_step):
    return int(time_step * basicTimeStep)

# Criação dos Sensores
# left_encoder = Encoder("left_rear_sensor", basicTimeStep, convert_time_to_time_step(encoder_update_time_ms))
# right_encoder = Encoder("right_rear_sensor", basicTimeStep, convert_time_to_time_step(encoder_update_time_ms))
gps1 = _GPS("gps_real_1", convert_time_to_time_step(gps_update_time_ms))
# gps2 = _GPS("gps_real_2", convert_time_to_time_step(gps_update_time_ms))
# mpu1 = MPU(1, convert_time_to_time_step(imu_update_time_ms))
# mpu2 = MPU(2, convert_time_to_time_step(imu_update_time_ms))

current_time_step = 0
while driver.step() != -1:

    current_time_step += 1

    # Realiza o movimento autonomo do robo
    # if (os.path.exists('stop_controller.txt')):
    #     print("O arquivo existe!!!")
    #     gps1.save()
    #     gps1.load() # printa o arquivo
    #     sys.exit(0)
    if (convert_time_step_to_time(current_time_step) >= 2000):
        print("Bateu o tempo")
        gps1.save()
        # gps1.load() # printa o arquivo
        sys.exit(0)
    else:
        robot_control.move()  

    # Obtencao dos valores dos sensores
    # wheel_ticks_values = left_encoder.get_ticks(), right_encoder.get_ticks()
    # accel1_values, gyro1_values, mag1_values = mpu1.get_accel(), mpu1.get_gyro(), mpu1.get_mag()
    # accel2_values, gyro2_values, mag2_values = mpu2.get_accel(), mpu2.get_gyro(), mpu2.get_mag()
    gps1_values = gps1.get_value()
    # gps2_values = gps2.get_value() 
    
        
    # print("Tempo execucao: ", str(convert_time_step_to_time(current_time_step)), "ms")
    if (current_time_step % convert_time_to_time_step(print_update_time_ms) == 0):
        # print("Tempo execucao: ", str(convert_time_step_to_time(current_time_step)), "ms", end="")
        # current_time_step = 0
        # print("GPS1" + str(gps1_values))
        print(convert_time_step_to_time(current_time_step), "ms ")
        gps1.update()
        # Visualizacao no terminal
        # print("Encoder" + str(wheel_ticks_values), end=" | ")
        # print("MPU1[" + str(accel1_values) + "g; " + str(gyro1_values) + "*/s; " + str(mag1_values) + "uT]", end=" | ")
        # # print("MPU2[" + str(accel2_values) + "g; " + str(gyro2_values) + "*/s; " + str(mag2_values) + "uT]", end=" | ")
        # print("GPS1" + str(gps1_values), end=" | ")
        # # print("GPS2" + str(gps2_values), end=" | ")

    # if (current_time_step % convert_time_to_time_step(30000) == 0):
    #     print("------------> SAVE")
    #     gps1.save()





    # print("Velocidade linear: " + str(robot_control.get_speed()) + " | Angulo: " + str(robot_control.get_angle())) 