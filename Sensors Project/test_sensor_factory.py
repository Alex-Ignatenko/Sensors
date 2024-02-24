import unittest
import sensor_factory
import sensors

class TestSensorFactory(unittest.TestCase):
    
    def setUp(self):
        self.tempFromFactory = sensor_factory.sensor_factory("TemperatureSensor","Temperature",0,100)
        self.humidityFromFactory = sensor_factory.sensor_factory("HumiditySensor","Humidity",0,100)
        self.pressureFromFactory = sensor_factory.sensor_factory("PressureSensor","Pressure",1000,1200)
        
        self.tempFromClass = sensors.Temp_Sensor("Temperature",0,100)
        self.humidityFromClass = sensors.Humidity_Sensor("Humidity",0,100)
        self.pressureFromClass = sensors.Pressure_Sensor("Pressure",1000,1200)

    def test_createInstance(self):
        self.assertIsInstance(self.tempFromFactory, sensors.Temp_Sensor)
        self.assertIsInstance(self.humidityFromFactory, sensors.Humidity_Sensor)
        self.assertIsInstance(self.pressureFromFactory, sensors.Pressure_Sensor)
        with self.assertRaises(TypeError):
            sensor_factory.sensor_factory("PresureSensor","Presure",1000,1200)

if __name__ == '__main__':
    unittest.main()