from controller import PositionSensor
import math

wheel_diameter_m = 0.1456
num_ticks = 4

class Encoder():
    def __init__(self, sensor_name, time_step):
        # Criação dos objetos Encoders
        self.sensor = PositionSensor(sensor_name)
        # Setup dos Encoders
        self.sensor.enable(time_step)
        self.init_last_tick = False
        
    def get_ticks(self):
        # Define o início como o marco zero
        if (not self.init_last_tick):
            self.last_tick = self.sensor.getValue()
            self.init_last_tick = True
        # Obtem a angulacao da roda desde o começo da simulacao
        current_radian_angle = self.sensor.getValue() - self.last_tick
        # Obtem a quantidade de ticks que houveram desde o inicio da simulacao (contando os ocorridos na re)
        tick = (current_radian_angle * num_ticks) / (2* math.pi)
        return int(tick)