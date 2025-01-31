#!/bin/bash

# Block an IP address using iptables
malicious_ip = "192.168.1.100"

echo "Blocking IP: $malicious_ip..."
sudo iptables -A INPUT -s $malicious_ip -j DROP

echo "IP address blocked successfully"