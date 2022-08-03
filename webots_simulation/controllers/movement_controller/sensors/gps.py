from controller import GPS
from sensors.data import Data

# Numero de casas para formatacao
# decimal_places = 6
# def format_digits(x, y, z):
#     return round(x, decimal_places), round(y, decimal_places), round(z, decimal_places)

class _GPS():
    def __init__(self, sensor_name, time_step):
        # Criação dos objetos Encoders
        self.sensor = GPS(sensor_name)
        # Setup dos GPS's
        self.sensor.enable(time_step)
        self.name = sensor_name
        self.current_step = 0
        self.update_step = time_step
        self.data = Data(sensor_name, size_sample=3)
    
    def update(self, repeat = 4):
        self.current_step += 1
        if (self.current_step >= self.update_step):
            # print("Update GPS")
            self.current_step = 0
            sample = self.get_value()
            for _ in range(0, repeat+1):
                self.data.update(sample)


    def save(self):
        self.data.save()
        
    def get_value(self):
        latitude, longitude, altitude = self.sensor.getValues()
        # return format_digits(latitude, longitude, altitude)
        return latitude, longitude, altitude