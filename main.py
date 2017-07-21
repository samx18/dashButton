# main program running as a background process
# run with sudo to enable netwrok capture

# import packages for scapy
from scapy.all import *

# Import packges for google API wrapper for google drive
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('myDrive-44b5c4114ddc.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("demo").sheet1

def arp_display(pkt):
	if pkt[ARP].op == 1: #who-has (request)
		if pkt[ARP].hwsrc == 'f0:27:2d:4b:c8:ef':
			print "Pushed G Button"
			print sheet.row_count
			now = datetime.datetime.now()
			date = now.strftime("%Y-%m-%d %H:%M")
			row =[date,"Button Pressed!"]
			sheet.append_row(row)
		else:
			print "Unknown probe"

print sniff(prn=arp_display, filter="arp", store=0)
