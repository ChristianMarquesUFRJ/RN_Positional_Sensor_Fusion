import random as rand
rand.seed(25)

PERCENT_TO_ROTATE = 0.99
PERCENT_OF_LINEAR_SPEED = 0.6

class autonomous_control():
    def __init__(self, driver):
        self.driver = driver
        #Velocidade incial e sua variação
        self.speed = 0
        self.speedOffset = 5
        #Angulo incial e sua variação
        self.angle =  0.0
        self.angleOffset = 0.1
        #Velocidade e angulo maximos
        self.maxSpeed = 50
        self.maxAngle = 0.9

    def get_speed(self):
        return self.speed
        
    def get_angle(self):
        return self.angle

    def get_speed_converted(self):
        return self.speed/13.889
        
    def get_angle_converted(self):
        # print("Tipo: ", type(self.angle), " | angulo: ", self.angle)
        return self.angle/1.34

    # Atualiza o angulo respeitando seus limites
    def update_angle(self, value):
        if ((value <= -self.maxAngle) or (value >= self.maxAngle)):
            return self.angle
        return value

    def move(self):
        # Velocidade linear constante em uma porcentagem alta em relacao a maxima
        self.speed = PERCENT_OF_LINEAR_SPEED * self.maxSpeed

        # Angulo (que gera a velocidade angular) gerado aleatoriamente
        value = rand.randrange(0, 100, 1)/100
        if (value >= PERCENT_TO_ROTATE):
            value = rand.randrange(0, 100, 1)/100
            if(value <= 0.44):
                self.angle = self.update_angle(self.angle+self.angleOffset)
                print("+", str(self.angleOffset))
            elif(value <= 0.88):
                self.angle = self.update_angle(self.angle-self.angleOffset)
                print("-", str(self.angleOffset))
            else:
                self.angle = 0.0
                print("+", str(self.angleOffset))
        else:
            print("0.0")

        # Controle do robo
        self.driver.setCruisingSpeed(self.get_speed_converted())
        self.driver.setSteeringAngle(self.get_angle_converted())
        