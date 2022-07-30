#Controlando o Atlas pelo teclado por enquanto

from vehicle import Driver
from movement.autonomous_control import autonomous_control
import os.path
import sys

driver = Driver()
basicTimeStep = int(driver.getBasicTimeStep())

robot_control = autonomous_control(driver)

while driver.step() != -1:
    # Realiza o movimento autonomo do robo
    if (os.path.exists('stop_controller.txt')):
        print("O arquivo existe!!!")
        sys.exit(0)
    else:
        robot_control.move()  




    # print("Velocidade linear: " + str(robot_control.get_speed()) + " | Angulo: " + str(robot_control.get_angle())) 