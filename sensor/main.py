#!/usr/bin/python

import gc  # garbage collector

from ldr import LDRSensor
from dht import DHTSensor
from sensor import VirtualSensor, Sensor
from sensorargs import _parser
from time import sleep


def main():
    _options = _parser.parse_args()

    if not _options.dht:
        dht = DHTSensor(_options.dht_model, _options.dht_pin)
    if not _options.ldr:
        ldr = LDRSensor(_options.ldr_pin)

    # virtual = VirtualSensor()
    # virtual1 = VirtualSensor(name='Second')

    print('reading...')
    while True:
        for o in gc.get_objects():
            if isinstance(o, Sensor):
                # prints all declared sensors
                print('{}: {}'.format(o.name,  o.read()))
        sleep(_options.period)


if __name__ == '__main__':
    main()
