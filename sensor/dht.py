import sys
import time
# import Adafruit_DHT
import csv
from .sensor import Sensor


class DHTSensor(Sensor):
    """docstring for DHTSensor"""

    def __init__(self, sensor_type, pin):
        super(DHTSensor, self).__init__(name='DHT')
        list_sensors = {
            '11': Adafruit_DHT.DHT11,
            '22': Adafruit_DHT.DHT22,
            '2302': Adafruit_DHT.AM2302,
            11: Adafruit_DHT.DHT11,
            22: Adafruit_DHT.DHT22,
            2302: Adafruit_DHT.AM2302,
        }
        if sensor_type in list_sensors.keys():
            self.sensor_type = list_sensors[sensor_type]
        else:
            raise Exception('Sensor type not valid')
        self.pin = pin

    def read_temperature(self):
        self.read()
        return self.temperature

    def read_humidity(self):
        self.read()
        return self.humidity

    def __read__(self):
        self.humidity, self.temperature = Adafruit_DHT.read_retry(
            self.sensor_type, self.pin)
        return self.humidity, self.temperature

    def __is_ok__(self):
        return True


if __name__ == '__main__':

    file = open('file.csv', 'w')
    wr = csv.writer(file, quoting=csv.QUOTE_ALL)

    # Parse command line parameters.
    sensor_args = {
        '11': Adafruit_DHT.DHT11,
        '22': Adafruit_DHT.DHT22,
        '2302': Adafruit_DHT.AM2302,
        11: Adafruit_DHT.DHT11,
        22: Adafruit_DHT.DHT22,
        2302: Adafruit_DHT.AM2302,
    }
    if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
        sensor = sensor_args[sys.argv[1]]
        pin = sys.argv[2]
    else:
        print('usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin')
        print(
            'example: sudo ./Adafruit_DHT.py 2302 4 - Lendo de um  AM2302 conectado ao GPIO')
        sys.exit(1)

    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

    print("*** Lendo os valores de temperatura e umidade")

    while True:
        if humidity is not None and temperature is not None:
            print(
                'Temperatura={0:0.1f}*  Humidade={1:0.1f}%'.format(temperature, humidity))
            wr.writerow([temperature, humidity])
            print("Aguarda 3 segundos para efetuar nova leitura...\n")
            time.sleep(3)
        else:
            print('Falha ao ler dados do DHT11. Tente Novamente!')
            sys.exit(1)
