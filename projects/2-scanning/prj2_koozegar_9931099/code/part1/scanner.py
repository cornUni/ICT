import socket
import argparse
from ip_scanner import IPScanner
from port_scanner import PortScanner
from utils import Protocols

def ip_scan(args):
    start_ip = args.ip[0]
    end_ip = args.ip[1]
    subnet_prefix = args.subnet_prefix

    ip_scanner = IPScanner(start_ip, end_ip, subnet_prefix)
    ip_scanner.scan_network()

def port_scan(args):
    protocol = Protocols.TCP if args.tcp else Protocols.UDP
    start_port, end_port = map(int, args.tcp if args.tcp else args.udp)

    port_scanner = PortScanner(start_port, end_port)
    port_scanner.scan_ports(protocol)
    


def main():
    parser = argparse.ArgumentParser(description="Simple network scanner")
    parser.add_argument("-m", "--subnet-prefix", type=int, help="Subnet prefix length (e.g., 24)")
    parser.add_argument("-ip", nargs=2, metavar=('start_ip', 'end_ip'), help="Start and end IP addresses")
    parser.add_argument("--ipscan", action="store_true", help="Start and end IP addresses")
    parser.add_argument("-portscan", action="store_true", help="port scan section")
    parser.add_argument("-tcp", nargs=2, metavar=('start_port', 'end_port'), help="Start and end port addresses")
    parser.add_argument("-udp", nargs=2, metavar=('start_port', 'end_port'), help="Start and end port addresses")

    args = parser.parse_args()
    if args.ipscan and (not args.subnet_prefix or not args.ip):
        print("Please provide both subnet prefix length (-m) and IP addresses (-ip)")
    elif args.ipscan:
        ip_scan(args)

    if args.portscan and not (args.tcp or args.udp):
        print("Please provide either TCP (-tcp) or UDP (-udp) start and end port values")
    elif args.portscan:
        port_scan(args)


if __name__ == "__main__":
    main()
