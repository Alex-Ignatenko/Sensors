import unittest
import main
import json
import sensors

class TestMain(unittest.TestCase):
    def setUp(self):
        self.tempFromClass = sensors.Temp_Sensor("TemperatureSensor",0,100)
        self.humidityFromClass = sensors.Humidity_Sensor("HumiditySensor",0,100)
        self.pressureFromClass = sensors.Pressure_Sensor("PressureSensor",900,1100)
        self.List_of_sensors = [self.tempFromClass, self.humidityFromClass, self.pressureFromClass]


    def test_init_sensors(self):
        test_data = {'sensors': [{'type': 'TemperatureSensor', 'valid_range': [0, 100]}, {'type': 'HumiditySensor', 'valid_range': [0, 100]}, {'type': 'PressureSensor', 'valid_range': [900, 1100]}]}
        sensors_from_func = main.init_sensors(test_data)    
        i=0
        for sensor in sensors_from_func:
            self.assertEqual(sensor.name, self.List_of_sensors[i].name)
            self.assertEqual(sensor.min_val, self.List_of_sensors[i].min_val)
            self.assertEqual(sensor.max_val, self.List_of_sensors[i].max_val)
            i +=1

    def test_setup_msgbus_pub(self):
         socket_url = "tcp://127.0.0.1:5500"
         test_context,test_socket = main.setup_msgbus_pub(socket_url)
         self.assertIsNotNone(test_context)
         self.assertIsNotNone(test_socket)

    def test_read_sensors(self):
        msg_list = main.read_sensors(self.List_of_sensors)
        for msg in msg_list:
            self.assertIsInstance(msg,str)

if __name__ == '__main__':
    unittest.main()