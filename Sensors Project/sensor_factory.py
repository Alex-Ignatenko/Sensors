import sensors

def sensor_factory(type,name,min_val, max_val):
    if type == "TemperatureSensor":
        return sensors.Temp_Sensor(name,min_val,max_val)
    elif type == "HumiditySensor":
        return sensors.Humidity_Sensor(name,min_val,max_val)
    elif type == "PressureSensor":
        return sensors.Pressure_Sensor(name,min_val,max_val)
    else:
        raise TypeError("Unrecognized sensor type.")