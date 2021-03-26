from scapy import *

pkts = scapy.sniff(iface="eth0", filter="host 10.3.1.42 and port 22", count=2)

print pkts
