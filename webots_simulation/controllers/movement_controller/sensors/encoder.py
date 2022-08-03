from controller import PositionSensor
import math

wheel_diameter_m = 0.1456
num_ticks = 4

class Encoder():
    def __init__(self, sensor_name, time_step, update_step):
        # Criação dos objetos Encoders
        self.sensor = PositionSensor(sensor_name)
        # Setup dos Encoders
        self.sensor.enable(time_step)
        self.init_last_tick = False

        self.update_step = update_step
        self.current_step = 0
        self.tick = 0
        
    def get_ticks(self):
        self.current_step += 1

        # Define o início como o marco zero
        if (not self.init_last_tick):
            self.last_tick = self.sensor.getValue()
            self.init_last_tick = True

        if (self.current_step % self.update_step == 0):
            self.current_step = 0
            # Obtem a angulacao da roda desde o começo da simulacao
            current_radian_angle = self.sensor.getValue() - self.last_tick

            # Obtem a quantidade de ticks que houveram desde o inicio da simulacao (contando os ocorridos na re)
            self.tick = (current_radian_angle * num_ticks) / (2* math.pi)

        return int(self.tick)