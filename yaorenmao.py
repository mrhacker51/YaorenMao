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
from Banners import fake_nmap_banner
from Banners import proxy_banner
from Banners import layer_seven_banner

## All Banners İnformation
# banner_started = start_banner.banner_one() ## Start Banner
# banner_whois = whois_banner.banner__whois() ## Whois Banner
# banner_nameserver = nameserver_banner.banner__nameserver() ## Nameserver Banner
# banner_traceroute = tracert_banner.banner__traceroute() ## Traceroute Banner
# banner_fake_nmap =  fake_nmap_banner.banner__nmap() ## Fake Nmap Scanner Banner
# banner_proxy = proxy_banner.banner__proxy() ## Proxy Banner
# banner_layer_seven = layer_seven_banner.banner__layer_seven() ## Layer 7 Banner

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



def options_proxy():
    print(colored.red("""[1] - ProxyScrape Website All """))


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



def get_proxy_scrape():
    response = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
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
                nameserver_ = İnformation(option)
                nameserver_ = nameserver_.nameserver_lookup()
                print(nameserver_)
                input("Press Enter Options")
                os.system("clear" if os.name == "nt" "cls" else "clear")

            elif option == "03":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_traceroute = tracert_banner.banner__traceroute()
                option = input("Enter İp Or Address : ")
                traceroute = İnformation(option)
                traceroute = traceroute.traceroute_lookup()
                print(traceroute)
                input("Press Enter Options")
                os.system("clear" if os.name == "nt" "cls" else "clear")

            elif option == "04":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_fake_nmap =  fake_nmap_banner.banner__nmap()

            elif option == "05":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_proxy = proxy_banner.banner__proxy()
                proxy_options = options_proxy()
                proxy = input("Enter Options Proxy : ")
                if proxy == "1":
                    scrape_proxy = get_proxy_scrape()
                    f = open("scrape-proxy.txt","w")
                    f.write(scrape_proxy)
                    f.close()
                    print("Successfully")
                    input("Press Enter Options")

            
            elif option == "06":
                os.system("clear" if os.name == "nt" "cls" else "clear")
                banner_layer_seven = layer_seven_banner.banner__layer_seven()
                option = input("Enter İp Or Address : ")

    except KeyboardInterrupt:
        sys.exit()
    except Exception as ex:
        print(ex)
        sys.exit()

