import zmq
import logging
import smtplib, ssl
from credentials import sender_email, sender_password

def setup_msgbus_sub(socket_url):
    """Create and configure a message bus publisher
       returns a socket object to publish messages to the bus
    """
    context = zmq.Context()
    socket =  context.socket(zmq.SUB)
    socket.connect(socket_url)
    socket.setsockopt_string(zmq.SUBSCRIBE,'')
    return context,socket

def get_logger():
    """Create and configure a logger
       returns logger instance to caller 
    """
    logging.basicConfig(filename="sensor_reads.log",format='%(asctime)s ::: %(levelname)s ::: %(message)s',level= logging.INFO,filemode='w')
    logger = logging.getLogger()
    return logger

def send_mail(sender_addr,sender_pass,reciever_addr,msg):
    """Send an email to a recipient"""
    body= str(msg)
    context = ssl.create_default_context() #manages settings and certificates for created sockets
    try:  
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as mail_connection: #use smtp lib secure ssl connection to send an email using a gmail account
            mail_connection.login(sender_addr,sender_pass)
            mail_connection.sendmail(sender_addr, 
                                        reciever_addr,
                                        msg="Subject: Sensor App Alert\n\n" + body)
    except smtplib.SMTPAuthenticationError:
        raise smtplib.SMTPAuthenticationError(1,"Sending mail failed check sender address or password")


def recieve_message(socket):
    """Recieve a message from the message bus
       prints the recieved message to the console
       returns the message to caller 
    """
    message=[]
    try:
        message = socket.recv_json(flags=zmq.NOBLOCK)
        print("Recieved message: " + message)
    except zmq.Again as e:
        #No messages received
        pass
    return message

def main():

    #define a url for the zmq socket and get a configured  message bus connection via context and socket objects
    socket_url = 'tcp://127.0.0.1:5000'
    context,socket=setup_msgbus_sub(socket_url)

    #configure a logger
    logger = get_logger()

    print("Alert serivce running...")

    #on a loop reads a message from the message bus and notifies user
    #loop closes on user key input
    #will close message bus connection after interrupt
    try:
        while True:    
            message = recieve_message(socket)
            if message:
                logger.warning(str(message))
                send_mail(sender_email,sender_password,sender_email,message)
    except KeyboardInterrupt:
            print('User forced exit')
    finally:
        socket.close()
        context.term()

if __name__ == '__main__':
    main()