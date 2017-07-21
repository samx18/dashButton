# Script for testing append to a google sheet

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
 
# Extract and print all of the val
#list_of_hashes = sheet.get_all_records()
#print(list_of_hashes)
print sheet.row_count
now = datetime.datetime.now()
date = now.strftime("%Y-%m-%d %H:%M")
row =[date,"Button Pressed!"]
index=1
#sheet.insert_row(row,index)
sheet.append_row(row)
