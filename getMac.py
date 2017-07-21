# Script to get MAC address of the button by capturing probes

# install additional packages 
# sudo apt-get install tcpdump tcpreplay wireshark
# sudo pip install scapy
# Run with sudo
# sudo python getMac.py

from scapy.all import *

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
   #if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
   print "ARP Probe from: " + pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=10)

