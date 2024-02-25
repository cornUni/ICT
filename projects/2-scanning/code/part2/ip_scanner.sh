#!/bin/bash

echo "Enter the IP range to scan (e.g., 192.168.1.0/24): "
read -r ip_range

echo "Scanning for active machines in the range $ip_range..."
nmap -sn "$ip_range" 
