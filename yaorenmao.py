## Library İmport
import requests
from bs4 import BeautifulSoup
from clint.textui import colored
import sys
import os

## Banners import 
from Banners import start_banner
from Banners import whois_banner
from Banners import nameserver_banner
from Banners import tracert_banner
# from Banners import fake_nmap_banner
# from Banners import proxy_banner
# from Banners import layer_seven_banner


## All Banners İnformation
# banner_started = start_banner.banner_one() ## Start Banner
# banner_whois = whois_banner.banner__whois() ## Whois Banner
# banner_nameserver = nameserver_banner.banner__nameserver() ## Nameserver Banner
# banner_traceroute = tracert_banner.banner__traceroute() ## Traceroute Banner


def options():
    my_string = ""
    print(colored.magenta(my_string.center(50,"-")))
    print(colored.red("""[01] - Whois Lookup """))
    print(colored.red("""[02] - NameServer Lookup """))
    print(colored.red("""[03] - Traceroute Lookup """))
    print(colored.red("""[04] - Fake Nmap İp & Mac Address Scanner Website """))
    print(colored.red("""[05] - Proxy Download """))
    print(colored.red("""[06] - Layer 7 Attack """))
    print(colored.red("""[99] - Exit """))
    print(colored.magenta(my_string.center(50,"-")))


class İnformation():
    def __init__(self,address):
        self.address = address
        self.url = "https://api.hackertarget.com"

    def whois_lookup(self):
        self.url = "https://www.whois.com/whois"
        response = requests.get(f"{self.url}/{self.address}")
        soup = BeautifulSoup(response.text,"html.parser")
        soup = soup.find("pre",{"class":"df-raw"})
        return soup.text

    def nameserver_lookup(self):
        response = requests.get(f"{self.url}/dnslookup/?q={self.address}")
        return response.text
    
    def traceroute_lookup(self):
        response = requests.get(f"{self.url}/mtr/?q={self.address}")
        return response.text




while True:
    banner_started = start_banner.banner_one()
    options()
    try:
        option = input("Enter Options : ")
        if option == "99":
            break
        else:
            if option == "01":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_whois = whois_banner.banner__whois()
                option = input("Enter İp Or Address : ")
                whois_ = İnformation(option)
                whois_ = whois_.whois_lookup()
                print(whois_)
                input("Press Enter Options")
                os.system("clear" if os.name == "nt" "cls" else "clear")

            elif option == "02":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_nameserver = nameserver_banner.banner__nameserver()
                option = input("Enter İp Or Address : ")

            elif option == "03":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_traceroute = tracert_banner.banner__traceroute()
                option = input("Enter İp Or Address : ")
    except KeyboardInterrupt:
        sys.exit()
    except Exception as ex:
        print(ex)
        sys.exit()
