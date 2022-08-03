#Controlando o Atlas pelo teclado por enquanto

from vehicle import Driver
from movement.autonomous_control import autonomous_control
from sensors.encoder import Encoders
from sensors.gps import _GPS
from sensors.mpu import MPU
import os.path
import sys

driver = Driver()
basicTimeStep = int(driver.getBasicTimeStep())

DATA_COLLECTION_TIME_SEG = 5
DATA_COLLECTION_TIME_STEP = DATA_COLLECTION_TIME_SEG*1000/basicTimeStep

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
encoders = Encoders("left_rear_sensor","right_rear_sensor", basicTimeStep, convert_time_to_time_step(encoder_update_time_ms))
# left_encoder = Encoder("left_rear_sensor", basicTimeStep, convert_time_to_time_step(encoder_update_time_ms))
# right_encoder = Encoder("right_rear_sensor", basicTimeStep, convert_time_to_time_step(encoder_update_time_ms))
gps1 = _GPS("gps_real_1", convert_time_to_time_step(gps_update_time_ms))
gps2 = _GPS("gps_real_2", convert_time_to_time_step(gps_update_time_ms))
mpu1 = MPU(1, convert_time_to_time_step(imu_update_time_ms))
mpu2 = MPU(2, convert_time_to_time_step(imu_update_time_ms))

current_time_step = 0
while driver.step() != -1:

    current_time_step += 1
    
    encoders.update()
    gps1.update()
    gps2.update()
    mpu1.update()
    mpu2.update()

    if (current_time_step >= DATA_COLLECTION_TIME_STEP):
        # print("Bateu o tempo")
        encoders.save()
        gps1.save()
        gps2.save()
        mpu1.save()
        mpu2.save()
        # gps1.load() # printa o arquivo
        sys.exit(0)
    else:
        robot_control.move()  



    # print("Velocidade linear: " + str(robot_control.get_speed()) + " | Angulo: " + str(robot_control.get_angle())) 