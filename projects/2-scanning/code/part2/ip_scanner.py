import nmap

def scan_ips(start_ip, end_ip):
    nm = nmap.PortScanner()

    ip_range = f"{start_ip}-{end_ip}"

    nm.scan(hosts=ip_range, arguments='-sn')

    for host in nm.all_hosts():
        if nm[host]['status']['state'] == 'up':
            print(f"Active IP found: {host}")

start_ip = "185.110.188.240"
end_ip = "185.110.188.255"

scan_ips(start_ip, end_ip)