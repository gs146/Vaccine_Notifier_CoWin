import requests
from datetime import date
import math

today = date.today()
d1 = today.strftime("%d-%m-%Y")

print("Enter your pincode: ")
pincode = int(input())

while True:
    digits = int(math.log10(pincode))+1
    if digits==6:
        break
    else:
        print("Invalid pin..Enter again:")
        pincode = int(input())


url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={0}&date={1}'.format(pincode,d1)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0'}
x = requests.get(url, headers=headers)
data = x.json()

#============================FOR 45+=======================================

cnt=1
listOfAllCentresFor45=[]

for d in data["sessions"]:
    if d["min_age_limit"] == 45:
        centre_detail = "Centre {0}: ".format(cnt) + "\nCentre Adrress: " + d['name'] + ", " + d["address"] + "\nVaccine: "+ d['vaccine'] + "\nAvailable Capacity dose 1: " + str(d["available_capacity_dose1"]) + "\nAvailable Capacity dose 2: " + str(d["available_capacity_dose2"]) + '\n'
        listOfAllCentresFor45.append(centre_detail)
        centre_detail=''
        cnt=cnt+1
        
# print(listOfAllCentresFor45)
if(len(listOfAllCentresFor45)==0):
     print("Vaccine for 45+ is not available!")
else:
    print("Are you 45+ .. then go and get ur vaccine!")


#============================FOR 18+=======================================

cnt=1
listOfAllCentresFor18=[]

for d in data["sessions"]:
    if d["min_age_limit"] == 18:
        centre_detail = "Centre {0}: ".format(cnt) + "\nCentre Adrress: " + d['name'] + ", " + d["address"] + "\nVaccine: " + d['vaccine'] + "\nAvailable Capacity dose 1: " + str(d["available_capacity_dose1"]) + "\nAvailable Capacity dose 2: " + str(d["available_capacity_dose2"]) + '\n'
        listOfAllCentresFor18.append(centre_detail)
        centre_detail=''
        cnt=cnt+1

if(len(listOfAllCentresFor18)==0):
     print("Vaccine for 18+ is not available!")
else:
    print("Are you 18+ .. then go and get ur vaccine!")


#============================Sending TELEGRAM MESSAGE=======================================

messageFor45 = ""

if len(listOfAllCentresFor45) >0:
    messageFor45 = messageFor45 + "*Available  vaccination centres for 45+:*\n\n"
    for mess in  listOfAllCentresFor45:
        messageFor45 = messageFor45 + mess
        messageFor45 = messageFor45 + "\n"

else:
    messageFor45 = messageFor45 + "*No slot available for 45 and above age*"

base_url = 'https://api.telegram.org/bot1845865793:AAF7slwdglakV31F5Q85JFAVf-KuyPCXIQ0/sendMessage?chat_id=-518514918&text={0}'.format(messageFor45)
print("Response:",requests.get(base_url))
print("Message Sent for 45+!")

#----------------------------------------------------------------------------
messageFor18 = ""

if len(listOfAllCentresFor18) >0:
    messageFor18 = messageFor18 + "*Available  vaccination centres for 18+:*\n\n"
    for mess in  listOfAllCentresFor18:
        messageFor18 = messageFor18 + mess
        messageFor18 = messageFor18 + "\n"

else:
    messageFor18 = messageFor18 + "*No slot available for 18 and above age*"

base_url = 'https://api.telegram.org/bot1845865793:AAF7slwdglakV31F5Q85JFAVf-KuyPCXIQ0/sendMessage?chat_id=-518514918&text={0}'.format(messageFor18)
print("Response:",requests.get(base_url))
print("Message Sent for 18+!")




        