

class key_control():
    def __init__(self, driver, time_step):
        #Velocidade incial e sua variação com o teclado
        self.speed = 0
        self.speedOffset = 5
        #Angulo incial e sua variação com o teclado
        self.angle = 0
        self.angleOffset = 0.1
        #Velocidade e angulo maximos
        self.maxSpeed = 50
        self.maxAngle = 0.9

        self.keyboard = driver.getKeyboard()
        self.keyboard.enable(4 * time_step)

    def get_speed(self):
        return self.speed/13.889
        
    def get_angle(self):
        return self.angle/1.34

    def update(self):
        currentKey = self.keyboard.getKey()
        forward = 0
        steer = 0
        while (currentKey != -1):
        #coleta de dados do teclado
            if currentKey == self.keyboard.UP:
                forward = 1
            elif currentKey == self.keyboard.DOWN:
                forward = -1
                
            if currentKey == self.keyboard.LEFT:
                steer = -1
            elif currentKey == self.keyboard.RIGHT:
                steer = 1
        #Fim da coleta de dados do teclado         
            currentKey = self.keyboard.getKey()
        
        #Setando a velocidade
        if forward == 0:
            if self.speed < 0.1 and self.speed > -0.1:
                self.speed = 0
            elif self.speed >= 0.1:
                self.speed -= self.speedOffset
            else:
                self.speed += self.speedOffset
        elif forward == 1:
            self.speed += self.speedOffset
        else:
            self.speed -= self.speedOffset
        
        #Setando angulo    
        if steer == 0:
            if self.angle < 0.1 and self.angle > -0.1:
                self.angle = 0
            elif self.angle >= 0.1:
                self.angle -= self.angleOffset
            else:
                self.angle += self.angleOffset
        elif steer == 1:
            self.angle += self.angleOffset
        else:
            self.angle -= self.angleOffset
            
        #limitando a velocidade e a angulacao maxima    
        if self.speed > self.maxSpeed:
            self.speed = self.maxSpeed
        elif self.speed < -1 * self.maxSpeed:
            self.speed = -1 * self.maxSpeed
        if self.angle > self.maxAngle:
            self.angle = self.maxAngle
        elif self.angle < -1 * self.maxAngle:
            self.angle = -1 * self.maxAngle
        