import socket
from utils import CliColors, Protocols ,print_color_string, save_report_file
class PortScanner():
    def __init__(self, start_port, end_port):
        self.start_port = start_port
        self.end_port = end_port
        self.target = '127.0.0.1'

    def scan_ports(self, protocol):
        socket_type = socket.SOCK_STREAM if protocol == Protocols.TCP else socket.SOCK_DGRAM
        report = ""
        print_color_string(f"Scanning {protocol} ports", CliColors.BOLD, CliColors.WARNING)
       
        for port in range(self.start_port, self.end_port+1):
            sock = socket.socket(socket.AF_INET, socket_type)
            sock.settimeout(1) 
            result = sock.connect_ex((self.target, port))
            

            if result == 0:
                data = f"{protocol} Port {port} is open"
                print_color_string(data, CliColors.OKGREEN, end= '\t------------>\t')
                service_name, message_color = self.get_service_name(port, protocol)
                report += data + '\t------------>\t' + service_name +'\n'
                print_color_string(service_name, message_color)
            else:
                data = f"{protocol} Port {port} is closed"
                report += data + '\n'
                print_color_string(data, CliColors.FAIL)
            sock.close()
        save_report_file(report, 'port_scan')


    def get_service_name(self, port, protocol):
        try:
            service = socket.getservbyport(port, protocol.lower())
            return service, CliColors.OKBLUE
        except OSError:
            return "Unable to retrieve service information", CliColors.FAIL

    
