# Script to test MAC address with button press

# Run with sudo
# sudo python buttonPress.py

from scapy.all import *

def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		#if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
		if pkt[ARP].hwsrc == 'f0:27:2d:4b:c8:ef':
			print "Pushed G Button"
		else:
			print "Unknown probe"

print sniff(prn=arp_display, filter="arp", store=0, count=10)

