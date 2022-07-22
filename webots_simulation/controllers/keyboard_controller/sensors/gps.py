from controller import GPS

# Numero de casas para formatacao
decimal_places = 6
def format_digits(x, y, z):
    return round(x, decimal_places), round(y, decimal_places), round(z, decimal_places)

class _GPS():
    def __init__(self, sensor_name, time_step):
        # Criação dos objetos Encoders
        self.sensor = GPS(sensor_name)
        # Setup dos GPS's
        self.sensor.enable(time_step)
        self.name = sensor_name
        
    def get_value(self):
        latitude, longitude, altitude = self.sensor.getValues()
        return format_digits(latitude, longitude, altitude)