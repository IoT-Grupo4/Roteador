from multiprocessing import Pool
from sensor import VirtualSensor, Sensor
from time import sleep
from controller import OSPFController


def check_sensor(sensor):
    return sensor.is_ok()


def main():

    # create virtual sensors for test
    sensors_list = [VirtualSensor('{}'.format(x)) for x in range(10)]

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
