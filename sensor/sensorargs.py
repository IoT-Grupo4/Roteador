import argparse
from os import path

_parser = argparse.ArgumentParser(
    usage="""python %(prog)s [OPTIONS]""",
    description="Read the sensors from a Raspberry Pi",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
)

# quiet options
_parser.add_argument("-q", "--quiet",
                     dest="verbose",
                     action="store_false",
                     help="suppress non error messages",
                     default=True
                     )

_parser.add_argument("--ldr-pin",
                     dest="ldr_pin",
                     type=int,
                     default=17,
                     help="Pin where the LDR is connected",
                     )

_parser.add_argument("--dht-pin",
                     dest="dht_pin",
                     type=int,
                     default=4,
                     help="Pin where the DHT is connected",
                     )

_parser.add_argument("--dht-model",
                     dest="dht_model",
                     type=int,
                     default=11,
                     choices=[11, 22, 2302],
                     help="Model of the DHT",
                     )

_parser.add_argument("--period",
                     dest="period",
                     type=float,
                     default=0.5,
                     help="Time, in seconds, the program will wait for a new read",
                     )

_parser.add_argument("--path",
                     dest="path",
                     type=str,
                     default=path.dirname(path.abspath(__file__)) + '/dados/',
                     help="Time, in seconds, the program will wait for a new read",
                     )

_parser.add_argument('-d', "--delimiter",
                     dest="delimiter",
                     type=str,
                     default=',',
                     help="Delimiter to CSV file",
                     )


_parser.add_argument("--no-ldr",
                     dest="ldr",
                     action="store_true",
                     help="Turn off LDR reading",
                     default=False
                     )

_parser.add_argument("--no-dht",
                     dest="dht",
                     action="store_true",
                     help="Turn off DHT reading",
                     default=False
                     )
