from controller import PositionSensor
import math
from sensors.data import Data

wheel_diameter_m = 0.1456
wheel_complete_turn_m = wheel_diameter_m * math.pi
num_ticks = 4
wheel_axis_m = 0.325

# Numero de casas para formatacao
# decimal_places = 4
# def format_digits(x, y):
#     return round(x, decimal_places), round(y, decimal_places)

class Encoders():
    def __init__(self, left_sensor_name, right_sensor_name, time_step, update_step):
        self.left_encoder = Encoder(left_sensor_name, time_step, update_step)
        self.right_encoder = Encoder(right_sensor_name, time_step, update_step)
        self.current_step = 0
        self.time_step = time_step
        self.update_step = update_step
        self.data = Data("encoders", size_sample=2)
    
    def get_wheel_speed(self, wheel_ticks):
        # Conversao de time_step em milissegundos
        dt_ms = (self.update_step * self.time_step)/1000
        # (PI * Diametro_roda)/(Numero_ticks_roda * dt) -> [m/s]
        speed = (wheel_complete_turn_m * wheel_ticks)/(num_ticks * dt_ms)
        # print("SPEED: ", str(speed), "m/s") 
        return speed

    def get_linear_and_angular_speed(self, left_wheel_ticks, right_wheel_ticks):
        left_speed, right_speed = self.get_wheel_speed(left_wheel_ticks), self.get_wheel_speed(right_wheel_ticks)
        # print(str(round(left_wheel_ticks,2)), " | ", str(round(right_wheel_ticks,2)))
        linear = (left_speed + right_speed)/2
        angular = (right_speed - left_speed)/wheel_axis_m
        # return format_digits(linear, angular)
        return linear, angular

    def save(self):
        self.data.save()
    
    def update(self):
        self.current_step += 1

        if (self.current_step >= self.update_step):
            print("Update encoder: ", end="")
            self.current_step = 0
            sample = self.get_linear_and_angular_speed(self.left_encoder.get_dTicks(), self.right_encoder.get_dTicks())
            # print(str(round(sample[0],2)), " | ", str(round(sample[1],2)))
            self.data.update(sample)
        
        

class Encoder():
    def __init__(self, sensor_name, time_step, update_step):
        # Criação dos objetos Encoders
        self.sensor = PositionSensor(sensor_name)
        # Setup dos Encoders
        self.sensor.enable(time_step)
        self.init_last_tick = False
        self.firt_tick = 0

        self.update_step = update_step
        self.current_step = 0
        self.tick = 0
        self.last_tick = 0
    
    def get_dTicks(self):
        self.tick = self.get_ticks()
        dTicks = self.tick - self.last_tick
        self.last_tick = self.tick
        return dTicks
        
    def get_ticks(self):

        # Define o início como o marco zero
        if (not self.init_last_tick):
            self.firt_tick = self.sensor.getValue()
            self.init_last_tick = True

    # if (self.current_step % self.update_step == 0):
        # self.current_step = 0
        # Obtem a angulacao da roda desde o começo da simulacao
        current_radian_angle = self.sensor.getValue() - self.firt_tick

        # Obtem a quantidade de ticks que houveram desde o inicio da simulacao (contando os ocorridos na re)
        return int((current_radian_angle * num_ticks) / (2* math.pi))