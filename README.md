The project simulates two services interacting with eachother

service one: represented by "main.py" is a sensor monitoring service
service two: represented by "alert.py" is a message sending service
add-ons: "sensors.py": a class lib used by the first service
         "sensor_factory.py": a factory that "main.py" uses to create diffrent sensor instances 
         "test_alert.py, test_main.py, test_sensor_factory.py": test files for corresponding components
         
- sensors.py: a class lib of diffrent sensors currently supports 3 types of sensors classes: temperature, humidty. and pressure all derive from a base sensor class
  each class includes the attributes:
    -name: name of the sensor of type str
    -min_val: min valid value the sensor reads of type int
    -max_val: max valid value the sensor reads of type int
  each class has a the method(s):
    -read_data: reads a value, each sensor overrides the base class method depending on its needs
     currently to simulate a read the function generates a random int value based on spesific sensor params

- sensor_factory.py: a factory that helps other components dynamicaly generate an isnatnce of a spesific sensor
  currently supports creation of temperature, humidity and pressure sensors
  on request of unsupported type will raise a type exception

- main.py: the sensor monitoring and validation service
  1.reads and parses a provided config file that tells it what sensors to create with which max and min valid values for each sensor
  2.creates instances of the needed sensors based on data from config file using the sensor factory
  3.on a loop reads the value from each initilized sensor each interval
  4.validates each value read if the result is invalid (higher or lower than given tresholds) sends a message to alert service via a message bus

 - alert.py: the user messaging service
   1.listens to the message bus
   2.when a message is recived notifys the user
     - logs the message into a logger
     - sends the message to the user email

  - Inter-Service Communication: the two services communicate using an instance of ZMQ message bus

run example:
 main.py: posts in console the generated messages:
 ![main consloe](https://github.com/Alex-Ignatenko/Sensors/assets/138715781/af4b94dd-cac3-49b2-8fba-2e221934b86e)

alert.py: posts in console the recieved message, creates a log entery and sends an email:
  cosole:
  ![alert console](https://github.com/Alex-Ignatenko/Sensors/assets/138715781/218b9092-37d9-4147-9a73-91b4b9d81cc8)

  log:
  ![log](https://github.com/Alex-Ignatenko/Sensors/assets/138715781/8abae691-112d-4080-9974-5b27c54c3336)

   
  mail:
  
  ![mail](https://github.com/Alex-Ignatenko/Sensors/assets/138715781/fb6b56f0-7546-4e74-a458-efc356eb754d)

  
  
  

  

         
