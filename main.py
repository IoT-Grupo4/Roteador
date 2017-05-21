from multiprocessing import Pool
from sensor import VirtualSensor, Sensor
from time import sleep
from controller import OSPFController
from sensor.ldr import LDRSensor
from sensor.dht import DHTSensor
from sensor.sensorargs import _parser


def check_sensor(sensor):
    return sensor.is_ok()


def main():

    # create virtual sensors for test
    _options = _parser.parse_args()
    sensors_list = [VirtualSensor('{}'.format(x)) for x in range(5)]

    # if not _options.dht:
    #     dht = DHTSensor(_options.dht_model, _options.dht_pin)
    # if not _options.ldr:
    #     ldr = LDRSensor(_options.ldr_pin)

    # list of all sensors
    sensors = Sensor.instances
    controller = OSPFController()

    print('Reading result of {} sensors'.format(len(sensors)))
    with Pool(1) as p:
        while True:
            result = [i.is_ok() for i in sensors]
            if False in result:
                pass  # TODO: altera prioridade
                print('Not OK                ', end='\r')
                controller.lower_priority()
            else:
                print('Everything is OK      ', end='\r')
                controller.raise_priority()
            sleep(_options.period)

if __name__ == '__main__':
    main()
