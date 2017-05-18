from .sensor import Sensor
from subprocess import run, PIPE
from re import findall


class TemperatureSensor(Sensor):
    """docstring for TemperatureSensor"""

    def __init__(self, name='Temperature'):
        super(TemperatureSensor, self).__init__(name)

    def __read__(self):
        cmd = ['vcgencmd', 'measure_temp']
        output = run(cmd, stdout=PIPE).stdout
        if len(output):
            return float(findall(r'([\d.]+)', output)[0])
        else
            return 0

    def __is_ok__(self):
        return self.__read__() < 60:
