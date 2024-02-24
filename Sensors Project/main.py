import json
import sensor_factory
from time import sleep 
import zmq

def read_config_file(file_name):
    """Read the configuration file return parsed dict."""
    with open(file_name) as config_file:
        config_data = json.load(config_file)
    return config_data

def init_sensors(config_data):
    """Initialize the list of active sensors based on the configuration"""
    active_sensors= []
    for i in config_data["sensors"]:
        #get the sensor type and min and max values from parsed config file for each sensor 
        sensor_type = i["type"]
        min_value = i["valid_range"][0]
        max_value = i["valid_range"][1]
        #append a sensor to sensor list, init sensor based on the values from each entery in config file
        active_sensors.append(sensor_factory.sensor_factory(sensor_type,sensor_type, min_value, max_value))
    return active_sensors

def setup_msgbus_pub(socket_url):
    """Create and configure a message bus publisher
       returns a socket object to publish messages to
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(socket_url)
    return context,socket

def send_message(socket,message):
    """Send a message to the message bus
        prints the sent message to the console
       Sends a json object, sends only if the message isn't empty  
    """
    if message:
        print("Sending message: ",message)
        messageJson = json.dumps(message)
        socket.send_json(messageJson)

def read_sensors(active_sensors):
    """Reads and validates the values of each active sensor
       returns a list of warning messages for each invalid read per sensor checked
    """
    messages = []
    sleep(5) 
    for i in active_sensors:
        current_read= i.read_data()
        if current_read < i.min_val:
            message = "DANGER! sensor: {}  value: {} is too low!".format(i.name,current_read)
            messages.append(message)
        elif current_read > i.max_val:
            message = "DANGER! sensor: {}  value: {} is too high!".format(i.name,current_read)
            messages.append(message) 
    return messages  

def main():
    
    #define a url for the zmq socket and get a configured  message bus connection via context and socket objects
    socket_url = 'tcp://127.0.0.1:5000'
    context,socket = setup_msgbus_pub(socket_url)

    #read the sensor config file and init sensor connectors based on config
    config_data= read_config_file("config.json")
    active_sensors = init_sensors(config_data)

    print("Main service running...")

    #on a loop reads values from the sensors and sends them to alert service via zmq message bus
    #loop closes on user key input
    #will close message bus connection after interrupt
    try:
        while True:   
            message = read_sensors(active_sensors)
            send_message(socket,message)
    except KeyboardInterrupt:
        print('User forced exit')
    finally:
        socket.close()
        context.term()

if __name__ == '__main__':
    main()