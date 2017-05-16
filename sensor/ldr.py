from gpiozero import LightSensor, Buzzer
from .sensor import Sensor


class LDRSensor(Sensor):
    """docstring for LDRSensor"""

    def __init__(self, pin):
        super(LDRSensor, self).__init__(name='LDR')
        self.pin = pin
        self.ldr = LightSensor(self.pin)  # alter if using a different pin
        self.ldr.wait_for_light(timeout=1)  # wait one second

    def __read__(self):
        return self.ldr.value

    def __is_ok__(self):
        return True

if __name__ == '__main__':
    ldr = LDRSensor(17)
    while True:
        print(ldr.read())
