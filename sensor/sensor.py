import logging
from os import path, makedirs
from .sensorargs import _parser
import weakref


_options = _parser.parse_args()


class NotImplemented(Exception):
    """Exception for Not implemented methods"""
    pass


class Sensor(object):
    """docstring for Sensor"""

    __instances__ = []

    def __init__(self, name, log_file=None, verbose=_options.verbose, delimiter=_options.delimiter, root=_options.path):
        super(Sensor, self).__init__()
        self.__class__.__instances__.append(weakref.proxy(self))
        self.name = name
        if log_file == None:
            log_file = name
        self.log_file = log_file
        self._delimiter_ = delimiter
        self._verbose_ = verbose
        if root is not None:
            self._root_ = root
        else:
            self._root_ = path.dirname(path.abspath(__file__))
        self.logger = None
        self._count_ = 0

    def read(self):
        value = self.__read__()
        self.log(value)
        return value

    def write(self, value):
        raise NotImplemented('Method for write values not Implemented')

    def is_ok(self):
        self.read()
        return self.__is_ok__()

    def __is_ok__(self):
        raise NotImplemented('Method for check values not Implemented')

    def close(self):
        pass

    def log(self, message):
        if not self._verbose_:
            return
        if not self.logger:
            self.__build_logger__()

        if (type(message) == list) or (type(message) == tuple):
            self.logger.info('{},'.format(self._count_) +
                             '{}'.format(self._delimiter_).join(
                                 str(i) for i in message)
                             )
        else:
            self.logger.info('{},{}'.format(self._count_, message))

        self._count_ += 1

    def __read__(self):
        raise NotImplemented('Method for read values not Implemented')

    def __build_logger__(self):
        """ Method to build the logger's handler """

        makedirs(self._root_, exist_ok=True)
        handler = logging.FileHandler(
            '%s/%s.csv' % (self._root_, self.log_file))

        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.INFO)

        # define a logging format
        formatter = logging.Formatter('%(message)s')
        handler.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(handler)
        return self.logger

    def __str__(self):
        return '{}'.format(self.__read__())

    def __inter__(self):
        return self.__instances__.__iter__()

    @classmethod
    def _get_sensors_(cls):
        return cls.__instances__


class VirtualSensor(Sensor):
    """docstring for VirtualSensor"""

    def __init__(self, name='Virtual'):
        super(VirtualSensor, self).__init__(name)

    def __read__(self):
        from random import randint
        return randint(0, 255), randint(0, 255)

    def __is_ok__(self):
        from random import choice
        return choice([True, False, True, True, True, True, True, True, True, True])
