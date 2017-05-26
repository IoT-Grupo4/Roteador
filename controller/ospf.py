from handlers.ConfigHandler import ConfigHandler
import subprocess


class OSPFController(object):
    """Send data to OSPF to control priority"""

    def __init__(self):
        # Quando raise_count chegar a três a rota deve ser aumentada
        # quanco chegar a -3 deve ser reduzida
        self.raise_count = 0
        self.ifaces = self.__discover_interfaces__()
        super(OSPFController, self).__init__()

    def __discover_interfaces__(self):
        # Descobre as interfaces do roteador e retorna uma lista com os nomes

        if_prefix = ConfigHandler.config["if_prefix"]

        # utilizamos a descoberta de vizinhos para identificar as interfaces
        # participantes
        quagga_command = "sh ip ospf neighbor"

        p1 = subprocess.Popen([
            "echo",
            quagga_command,
        ], stdout=subprocess.PIPE)

        p2 = subprocess.Popen([
            "vtysh"
        ], stdin=p1.stdout, stdout=subprocess.PIPE)

        p3 = subprocess.Popen([
            "grep",
            "-v",
            "-P",
            "^ ",
        ], stdin=p2.stdout, stdout=subprocess.PIPE)

        p4 = subprocess.Popen([
            "grep",
            if_prefix
        ], stdin=p3.stdout, stdout=subprocess.PIPE)

        p5 = subprocess.Popen([
            "awk",
            "{print $6}"
        ], stdin=p4.stdout, stdout=subprocess.PIPE)

        p6 = subprocess.Popen([
            "awk",
            "-F",
            ":",
            "{print $1}"
        ], stdin=p5.stdout, stdout=subprocess.PIPE)

        result = p6.communicate()
        ifaces = result[0].decode('utf-8').rstrip().split("\n")
        print('interfaces descobertas: ')
        print(ifaces)
        return ifaces

    def __set_priority__(self, if_name, cost):

        quagga_command = """
            conf t
            int {0}
            ip ospf cost {1}
            exit
        """.format(if_name, cost)

        p1 = subprocess.Popen([
            "echo",
            quagga_command
        ], stdout=subprocess.PIPE)

        p2 = subprocess.Popen([
            "vtysh"
        ], stdin=p1.stdout, stdout=subprocess.PIPE)

    def raise_priority(self):
        # raise_priority == lower_cost
        self.raise_count += 1

        cost_increment = ConfigHandler.config["cost_increment"]
        delay_increment = ConfigHandler.config["delay_increment"]

        if self.raise_count >= delay_increment:

            # Interefere no custo de todas as interfaces
            for iface in self.ifaces:
                print('reduzindo custo para interface {0}'.format(iface))
                current_cost = self.get_priority(iface)
                new_cost = current_cost - cost_increment
                self.__set_priority__(iface, new_cost)

            self.raise_count = 0

    def lower_priority(self):
        # lower_priority == raise_cost
        self.raise_count -= 1

        delay_increment = 0 - int(ConfigHandler.config["delay_increment"])
        cost_increment = ConfigHandler.config["cost_increment"]

        if self.raise_count <= delay_increment:

            # Interefere no custo de todas as interfaces
            for iface in self.ifaces:
                print('aumentando custo para interface {0}'.format(iface))
                iface = 'enp0s8'
                current_cost = self.get_priority(iface)
                new_cost = current_cost + cost_increment
                self.__set_priority__(iface, new_cost)

            self.raise_count = 0

    def get_priority(self, if_name):

        if if_name == "" or if_name == None:
            raise InvalidInterface("Interface name must be a valid string")
            return

        quagga_command = "sh ip ospf interface {0}".format(if_name)

        p1 = subprocess.Popen([
            "echo",
            quagga_command
        ], stdout=subprocess.PIPE)

        p2 = subprocess.Popen([
            "vtysh"
        ], stdin=p1.stdout, stdout=subprocess.PIPE)

        p3 = subprocess.Popen([
            "grep",
            "Cost"
        ], stdin=p2.stdout, stdout=subprocess.PIPE)

        p4 = subprocess.Popen([
            "awk",
            "-F",
            ", ",
            "{print $3}"
        ], stdin=p3.stdout, stdout=subprocess.PIPE)

        p5 = subprocess.Popen([
            "awk",
            "-F",
            ": ",
            "{print $2}"
        ], stdin=p4.stdout, stdout=subprocess.PIPE)

        result = p5.communicate()
        result = int(result[0].decode('utf-8'))

        if result > 0:
            return result
        else:
            raise InvalidCost('Interface Cost must be a non-zero integer')
