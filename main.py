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
    sensors_list = [VirtualSensor('{}'.format(x)) for x in range(10)]
    _options = _parser.parse_args()

    if not _options.dht:
        dht = DHTSensor(_options.dht_model, _options.dht_pin)
    if not _options.ldr:
        ldr = LDRSensor(_options.ldr_pin)

    # list of all sensors
    sensors = Sensor.instances
    controller = OSPFController()

    print('Reading result of {} sensors'.format(len(sensors)))
    with Pool() as p:
        while True:
            result = p.map(check_sensor, sensors)
            if False in result:
                pass  # TODO: altera prioridade
                print('Not OK                ', end='\r')
            else:
                print('Everything is OK      ', end='\r')
                pass  # TODO: coloca prioridade em default
            sleep(0.1)

if __name__ == '__main__':
    main()
