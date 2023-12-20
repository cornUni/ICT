import socket
from utils import CliColors, print_color_string, save_report_file


class IPScanner():
    def __init__(self, start_ip, end_ip, subnet_prefix):
        self.start_ip = start_ip
        self.end_ip = end_ip
        self.subnet_prefix = subnet_prefix
        


    def scan_network(self):
        ip_range = self.__get_ip_range()
        report = ""
    
        print_color_string("Scanning IPs...", CliColors.BOLD, CliColors.WARNING)
        for ip in ip_range:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)
            try:
                sock.connect((ip.split('/')[0], 80)) 
                data = f"IP {ip} is active"
                report += data +'\n'
                print_color_string(data, CliColors.OKGREEN)
            except socket.error:
                data = f'IP {ip} is not active'
                report += data +'\n'
                print_color_string(data, CliColors.FAIL)
            finally:
                save_report_file(report, 'network_IP_scan')
                sock.close()
    
    def __get_ip_range(self):
        start = self.__ip_to_int(self.start_ip)
        end = self.__ip_to_int(self.end_ip)
        ip_range = [self.__int_to_ip(i) for i in range(start, end + 1)]
        return [ip + f'/{self.subnet_prefix}' for ip in ip_range]
    
    def __ip_to_int(self, ip):
        parts = ip.split('.')
        return (int(parts[0]) << 24) + (int(parts[1]) << 16) + (int(parts[2]) << 8) + int(parts[3])
    
    def __int_to_ip(self, n):
        return f"{(n >> 24) & 255}.{(n >> 16) & 255}.{(n >> 8) & 255}.{n & 255}"
            