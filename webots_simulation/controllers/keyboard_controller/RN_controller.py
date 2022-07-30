#Controlando o Atlas pelo teclado por enquanto

from vehicle import Driver
from teclado.keyboard_control import key_control
from sensors.encoder import Encoder
from sensors.gps import _GPS
from sensors.mpu import MPU

driver = Driver()
basicTimeStep = int(driver.getBasicTimeStep())

robot_control = key_control(driver, basicTimeStep)

# Criação dos Sensores
left_encoder = Encoder("left_rear_sensor",basicTimeStep)
right_encoder = Encoder("right_rear_sensor",basicTimeStep)
gps1 = _GPS("gps_real_1",basicTimeStep)
gps2 = _GPS("gps_real_2",basicTimeStep)
mpu1 = MPU(1,basicTimeStep)
mpu2 = MPU(2,basicTimeStep)

while driver.step() != -1:
    # Atualizacao dos dados do teclado
    robot_control.update()    
    
    # Controle do robo
    # speed_robot, speed_mph = robot_control.speed
    # driver.setCruisingSpeed(speed_mph)
    driver.setCruisingSpeed(robot_control.get_speed())
    driver.setSteeringAngle(robot_control.get_angle())
    
    # Obtencao dos valores dos sensores
    wheel_ticks_values = left_encoder.get_ticks(), right_encoder.get_ticks()
    accel1_values, gyro1_values, mag1_values = mpu1.get_accel(), mpu1.get_gyro(), mpu1.get_mag()
    accel2_values, gyro2_values, mag2_values = mpu2.get_accel(), mpu2.get_gyro(), mpu2.get_mag()
    gps1_values = gps1.get_value()
    gps2_values = gps2.get_value()
    
    # Visualizacao no terminal
    # print("Encoder" + str(wheel_ticks_values), end=" | ")
    # print("MPU1[" + str(accel1_values) + "g; " + str(gyro1_values) + "*/s; " + str(mag1_values) + "uT]", end=" | ")
    # # print("MPU2[" + str(accel2_values) + "g; " + str(gyro2_values) + "*/s; " + str(mag2_values) + "uT]", end=" | ")
    # print("GPS1" + str(gps1_values), end=" | ")
    # # print("GPS2" + str(gps2_values), end=" | ")
    # print("")