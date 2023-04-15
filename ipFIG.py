import requests
from colorama import Fore,Style

print(F"""{Fore.CYAN}
   ____     ____                
  /  _/__  / __/__  ___________ 
 _/ // _ \/ _// _ \/ __/ __/ -_)
/___/ .__/_/  \___/_/  \__/\__/ 
   /_/                               
                   {Style.RESET_ALL} Coded By Yigoboz | https://github.com/
""")

def check():
    r = requests.get("https://ipinfo.io/")
    print(F"\n {Fore.YELLOW} Database checking... {Style.RESET_ALL}\n")
    if r.status_code == 200:
        print(F"{Fore.GREEN} [+] Database is active! {Style.RESET_ALL} \n")
    else:
        print(F"\n {Fore.RED} [!] Database is not active  {Style.RESET_ALL} \n")
        print(F" {Fore.RED} [?] Exiting..... {Style.RESET_ALL}")
        exit()

try:
    ip = input("Target Ip: ")
    check()
    country = requests.get("https://ipinfo.io/{}/country/".format(ip)).text
    city = requests.get("https://ipinfo.io/{}/city/".format(ip)).text
    region = requests.get("https://ipinfo.io/{}/region/".format(ip)).text
    postal = requests.get("https://ipinfo.io/{}/postal/".format(ip)).text
    timezone = requests.get("https://ipinfo.io/{}/timezone/".format(ip)).text
    orgination = requests.get("https://ipinfo.io/{}/org/".format(ip)).text
    location =  requests.get("https://ipinfo.io/{}/loc/".format(ip)).text

    print(F"{Fore.GREEN} İp: {Style.RESET_ALL}"+ip)
    print(F"{Fore.GREEN} Country: {Style.RESET_ALL}"+country)
    print(F"{Fore.GREEN} City: {Style.RESET_ALL}"+city)
    print(F"{Fore.GREEN} Region: {Style.RESET_ALL}"+region)
    print(F"{Fore.GREEN} Postal: {Style.RESET_ALL}"+postal)
    print(F"{Fore.GREEN} TimeZone: {Style.RESET_ALL}"+timezone)
    print(F"{Fore.GREEN} Orgination: {Style.RESET_ALL}"+orgination)
    print(F"{Fore.GREEN} Location: {Style.RESET_ALL}"+location)
except KeyboardInterrupt:
    print(F"\n {Fore.RED} CTRL+C Detected! {Style.RESET_ALL}")
