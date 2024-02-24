import unittest
import alert
import smtplib


class TestAlert(unittest.TestCase):

    def test_setup_msgbus_sub(self):
         socket_url = "tcp://127.0.0.1:5500"
         test_context,test_socket = alert.setup_msgbus_sub(socket_url)
         self.assertIsNotNone(test_context)
         self.assertIsNotNone(test_socket)

    def test_send_mail(self):
            test_mail = "test@gmail.com"
            test_pwd = "testpw"
            with self.assertRaises(smtplib.SMTPAuthenticationError):
                alert.send_mail(test_mail, test_pwd,test_mail,"test")

if __name__ == '__main__':
    unittest.main()