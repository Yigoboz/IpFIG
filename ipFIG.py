import requests



print("""
   ____     ____                
  /  _/__  / __/__  ___________ 
 _/ // _ \/ _// _ \/ __/ __/ -_)
/___/ .__/_/  \___/_/  \__/\__/ 
   /_/                               
                    Coded By Yigoboz | https://github.com/
""")

def check():
    r = requests.get("https://ipinfo.io/")
    print("\n Database checking...\n")
    if r.status_code == 200:
        print("[+] Database is active! \n")
    else:
        print("\n [!] Database is not active \n")
        print("[?] Exiting.....")
        exit()

ip = input("Target Ip: ")

check()

country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text
city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text
region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text

print("İp: "+ip)
print("Country: "+country)
print("City: "+city)
print("Region: "+region)
print("Postal: "+postal)
print("TimeZone: "+timezone)
print("Orgination: "+orgination)
print("Location: "+location)