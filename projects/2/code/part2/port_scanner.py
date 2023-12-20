import nmap

def scan_ports():
    nm = nmap.PortScanner()

    port_range = "1-1024"  

    nm.scan('localhost', arguments=f'-p {port_range}')

    for host in nm.all_hosts():
        print(f"Scanning ports for host: {host}")
        for proto in nm[host].all_protocols():
            print(f"Protocol: {proto}")
            ports = nm[host][proto].keys()
            for port in ports:
                port_info = nm[host][proto][port]
                print(f"Port: {port} \tState: {port_info['state']} \tService: {port_info['name']} \tProtocol: {proto}")


scan_ports()
