import random

class Sensor:
    def __init__(self, name,min_val, max_val):
        self.name = name
        self.min_val = min_val
        self.max_val = max_val
    
    def read_data(self):
        pass

class Temp_Sensor(Sensor):
    def __init__(self,name,min_val, max_val):
        Sensor.__init__(self,name,min_val, max_val)

    def read_data(self):
        return random.randrange(-50, 120, 5)

class Humidity_Sensor(Sensor):
    def __init__(self,name,min_val, max_val):
        Sensor.__init__(self,name,min_val, max_val)

    def read_data(self):
        return random.randrange(-20, 120, 10)

class Pressure_Sensor(Sensor):
    def __init__(self,name,min_val, max_val):
        Sensor.__init__(self,name,min_val, max_val)

    def read_data(self):
        return random.randrange(500, 1500, 100)