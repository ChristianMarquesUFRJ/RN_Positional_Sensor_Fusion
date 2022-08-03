from controller import Accelerometer, Gyro, Compass
import math
from sensors.data import Data

# Acelaracao da gravidade
g = 9.807

# Numero de casas para formatacao
# decimal_places = 4
# def format_digits(x, y, z):
#     return round(x, decimal_places), round(y, decimal_places), round(z, decimal_places)

class Acelerometro():
    def __init__(self, sensor_name, time_step):
        # Criação dos objetos Encoders
        self.acelerometro = Accelerometer(sensor_name)
        # Setup dos GPS's
        self.acelerometro.enable(time_step)
        
    def get_value(self):
        # Obtem valores em m/s²
        x, y, z = self.acelerometro.getValues()
        # Converte em G's
        x, y, z = x/g, y/g, z/g
        # return format_digits(x, y, z)
        return x, y, z

class _Gyro():
    def __init__(self, sensor_name, time_step):
        # Criação dos objetos Encoders
        self.giroscopio = Gyro(sensor_name)
        # Setup dos GPS's
        self.giroscopio.enable(time_step)
        
    def get_value(self):
        # Obtem valores em rad/s
        x, y, z = self.giroscopio.getValues()
        # Converte em graus/s
        x, y, z = math.degrees(x), math.degrees(y), math.degrees(z)
        # return format_digits(x, y, z)
        return x, y, z

class Magnetometro():
    def __init__(self, sensor_name, time_step):
        # Criação dos objetos Encoders
        self.magnetometro = Compass(sensor_name)
        # Setup dos GPS's
        self.magnetometro.enable(time_step)
           
    def get_value(self):
        # Obtem 3 valores de -1 a 1
        x, y, z = self.magnetometro.getValues()

        def converter_uT(value):
            return value*0.6/128

        # Converte em microTesla
        x, y, z = converter_uT(x), converter_uT(y), converter_uT(z)
        # return format_digits(x, y, z)
        return x, y, z


class MPU():
    def __init__(self, mpu_number, time_step):
        # Criação dos sensores pertencentes ao MPU
        self.accel = Acelerometro("acelerometro_"+str(mpu_number), time_step)
        self.gyro = _Gyro("giroscopio_"+str(mpu_number), time_step)
        self.mag = Magnetometro("magnetometro_"+str(mpu_number), time_step)
        self.current_step = 0
        self.update_step = time_step
        self.data = Data("mpu_"+str(mpu_number), size_sample=9)
    
    def update(self):
        self.current_step += 1
        if (self.current_step >= self.update_step):
            # print("Update MPU")
            self.current_step = 0
            sample = self.get_accel() + self.get_gyro() + self.get_mag()
            self.data.update(sample)

    def save(self):
        self.data.save()
        
    def get_accel(self):
        return self.accel.get_value()

    def get_gyro(self):
        return self.gyro.get_value()

    def get_mag(self):
        return self.mag.get_value()