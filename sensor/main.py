#!/usr/bin/python

import gc  # garbage collector

from ldr import LDRSensor
from dht import DHTSensor
from sensor import VirtualSensor, Sensor
from sensorargs import _parser
from time import sleep


def main():

    # create virtual sensors for test
    _options = _parser.parse_args()
    sensors_list = [VirtualSensor('{}'.format(x)) for x in range(5)]

    if not _options.dht:
        dht = DHTSensor(_options.dht_model, _options.dht_pin)
    if not _options.ldr:
        ldr = LDRSensor(_options.ldr_pin)

    # list of all sensors
    sensors = Sensor._get_sensors_()

    print('Reading result of {} sensors'.format(len(sensors)))
    while True:
        result = [i.is_ok() for i in sensors]
        if False in result:
            pass  # TODO: altera prioridade
            print('Not OK                ', end='\r')
        else:
            print('Everything is OK      ', end='\r')
        sleep(_options.period)


if __name__ == '__main__':
    main()
