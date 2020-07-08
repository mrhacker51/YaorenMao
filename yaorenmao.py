## Library İmport
import requests
from bs4 import BeautifulSoup
from clint.textui import colored
import sys
import os
import time


# Nmap Library
import nmap3

# Selenium Library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options


# Clear System Function

def clear():
    os.system("clear" if os.name == "nt" "cls" else "clear")

## Clear System Function



## Selenium Clientless Options
selenium_options =   Options()
selenium_options.headless = True
driver_path = "/opt/YaorenMao/geckodriver"
browser_path = "/opt/YaorenMao/firefox"

if not os.path.exists(driver_path) or not os.path.exists(browser_path):
    sys.stdout.write(str(colored.red("\n[+] Please put the tool in [Opt Folder + Run Setup.sh ]\n")))
    sys.stdout.flush()
    sys.exit()
else:
    pass

## Banners import 
from Banners import start_banner
from Banners import whois_banner
from Banners import nameserver_banner
from Banners import tracert_banner
from Banners import fake_nmap_banner
from Banners import proxy_banner
from Banners import layer_seven_banner
from Banners import waf_banner
from Banners import subdomain_banner
from Banners import social_banner

"""
________________________________
____***_YAORENMAO TOOLS ***____
"""

## Menü Options : 
def options():
    my_string = ""
    print(colored.magenta(my_string.center(50,"▬")))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [01] - [*] Whois Lookup """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [02] - [*] NameServer Lookup """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [03] - [*] Traceroute Lookup """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [04] - [*] Fake Nmap İp & Mac Address Scanner Website """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [05] - [*] Proxy Download """))
    print(colored.blue("""\t▬▬▬▬▬▬▬▬ [06] - [*] Layer 7 Attack """))
    print(colored.blue("""\t▬▬▬▬▬▬▬▬ [07] - [*] SubDomain Finder """))
    print(colored.blue("""\t▬▬▬▬▬▬▬▬ [08] - [*] WAF Checker """))
    print(colored.blue("""\t▬▬▬▬▬▬▬▬ [09] - [*] Social Media Finder """))
    print(colored.blue("""\t▬▬▬▬▬▬▬▬ [99] - [*] Exit """))
    print(colored.magenta(my_string.center(50,"▬")))


## Proxy Menü Options : 
def options_proxy():
    my_string = ""
    print(colored.magenta(my_string.center(50,"▬")))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [1]  - [*] ProxyScrape Website [ + Socks5 ] """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [2]  - [*] Proxy-List Website  [ + Socks5 ] """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [3]  - [*] ProxyScrape Website [ + Socks4 ] """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [4]  - [*] Proxy-List Website  [ + Socks4 ] """))
    print(colored.red("""\t▬▬▬▬▬▬▬▬ [99] - [*] Exit """))
    print(colored.magenta(my_string.center(50,"▬")))


def options_nmap():
    my_string = ""
    print(colored.magenta(my_string.center(50,"▬")))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [1]  - [*] DNS BRUTE   """))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [2]  - [*] TCP SCANNER """))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [3]  - [*] UDP SCANNER """))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [4]  - [*] PING        """))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [5]  - [*] SUBNET SCANNER        """))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [6]  - [*] FAKE IP SCANNER        """))
    print(colored.yellow("""\t▬▬▬▬▬▬▬▬ [99] - [*] Exit        """))
    print(colored.magenta(my_string.center(50,"▬")))



## İnformation ##
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


#################### Proxy Request Started ####################
def get_proxy_scrape():
    response = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks5&country=all")
    return response.text

def get_proxy_proxy_list():
    response = requests.get("https://www.proxy-list.download/api/v1/get?type=socks5")
    return response.text

def get_proxy_scrape_socks4():
    response = requests.get("https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&country=all")
    return response.text

def get_proxy_proxy_list_socks4():
    response = requests.get("https://www.proxy-list.download/api/v1/get?type=socks4")
    return response.text

#################### Proxy Finished ###########################


## Selenium Sub Domain - Waf Finder // 
class Seleniumİnformation():
    def __init__(self,address):
        self.url = "https://www.nmmapper.com"
        self.address = address
        self.driver = webdriver.Firefox(options=selenium_options,executable_path=driver_path)
        #self.driver = webdriver.Firefox(executable_path=driver_path)

    def selenium_subdomain(self):
        self.driver.get(f"{self.url}/sys/tools/subdomainfinder/")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='Enumhost']").send_keys(f"{self.address}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='start-scan']").click()
        time.sleep(2)

        subdomain_scanner = self.driver.find_elements_by_id("subdomain-tbody")

        for subdomains in subdomain_scanner:
            if "OOps nothing found" in subdomains.text:
                sys.stdout.write(str(colored.red("[-] Sub Domain Not Found !")))
                sys.stdout.flush()
            else:
                print(colored.red("[ + HOST ]") + " " + colored.yellow("[ + SubDomain ]") + " " + colored.green("[ + IP ]") + " " + colored.magenta("[ + ASN ]"))
                print(colored.green(subdomains.text))
                time.sleep(1)

        self.driver.close()



    def selenium_wafchecker(self):
        self.driver.get(f"{self.url}/tools/reconnaissance-tools/waf/web-application-firewall-detector/")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='ep-wafdetector']").send_keys(f"{self.address}")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='start-scan']").click()

        waf_scanner = self.driver.find_elements_by_xpath("//*[@id='wafdetector-tbody']")

        for wafs in waf_scanner:
            print(colored.red("[ + HOST ]") + " " + colored.yellow("\t[ + IP ]") + " " + colored.green("\t[ + WAF ]"))
            time.sleep(8)
            print(colored.green(wafs.text))

            if not wafs.text:
                print(colored.red("[-] Waf Not Found "))
        time.sleep(3)
        self.driver.close()


## Nmap Started

class NmapFunction():
    def __init__(self,address):
        self.address = address
    
    def dns_nmap(self):
        nmap = nmap3.Nmap()
        result = nmap.nmap_dns_brute_script(f"{self.address}")
        print(colored.green("[ + ] HOST ") + "" + "\t" + "\t" + colored.blue("[ + ] IP "))
        for i in result:
            text = i["hostname"] + "\t" + i["address"]
            print(text)

    def tcp_scanner_nmap(self):
        nmap = nmap3.NmapScanTechniques()
        result = nmap.nmap_tcp_scan(f"{self.address}")

    def udp_scanner_nmap(self):
        result = nmap.nmap_tcp_scan(f"{self.address}")

    def ping_nmap(self):
        result = nmap.nmap_tcp_scan(f"{self.address}")

    def subnet_scanner_nmap(self):
        result = nmap.nmap_tcp_scan(f"{self.address}")

    def fake_scanner_nmap(self):
        result = nmap.nmap_tcp_scan(f"{self.address}")



## Social Media Started ###

class SocialMedia():
    def __init__(self,address):
        self.address = address

    def facebook(self):
        response = requests.get(f"https://www.facebook.com/{self.address}")
        if response.status_code == 200:
            return sys.stdout.write(str(colored.yellow(f"\n[+] https://www.facebook.com/{self.address}")))
            return sys.stdout.flush()
        else:
            return sys.stdout.write(str(colored.red(f"\n[-] https://www.facebook.com/{self.address}")))
            return sys.stdout.flush()

    def instagram(self):
        response = requests.get(f"https://www.instagram.com/{self.address}/")
        if response.status_code == 200:
            return sys.stdout.write(str(colored.yellow(f"\n[+] https://www.instagram.com/{self.address}")))
            return sys.stdout.flush()
        else:
            return sys.stdout.write(str(colored.red(f"\n[-] https://www.instagram.com/{self.address}")))
            return sys.stdout.flush()


    def github(self):
        response = requests.get(f"https://www.github.com/{self.address}/")
        if response.status_code == 200:
            return sys.stdout.write(str(colored.yellow(f"\n[+] https://www.github.com/{self.address}")))
            return sys.stdout.flush()
        else:
            return sys.stdout.write(str(colored.red(f"\n[-] https://www.github.com/{self.address}")))
            return sys.stdout.flush()


    def twitter(self):
        response = requests.get(f"https://www.twitter.com/{self.address}/")
        if response.status_code == 200:
            return sys.stdout.write(str(colored.yellow(f"\n[+] https://www.twitter.com/{self.address}")))
            return sys.stdout.flush()
        else:
            return sys.stdout.write(str(colored.red(f"\n[-] https://www.twitter.com/{self.address}")))
            return sys.stdout.flush()



    def youtube(self):
        response = requests.get(f"https://www.youtube.com/user/{self.address}")
        if response.status_code == 200:
            return sys.stdout.write(str(colored.yellow(f"\n[+] https://www.youtube.com/user/{self.address}")))
            return sys.stdout.flush()
        else:
            return sys.stdout.write(str(colored.red(f"\n[-] https://www.youtube.com/user/{self.address}")))
            return sys.stdout.flush()

## Social Media Finished ###


while True:
    banner_started = start_banner.banner_one()
    options()
    try:
        option = input("Enter Options : ")
        if option == "99":
            break
        else:
            if option == "01":
                clear()
                banner_whois = whois_banner.banner__whois()
                option = input("Enter İp / Host : ")
                whois_ = İnformation(option)
                whois_ = whois_.whois_lookup()
                print(whois_)
                input("▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")
                clear()

            elif option == "02":
                clear()
                banner_nameserver = nameserver_banner.banner__nameserver()
                option = input("Enter İp / Host : ")
                nameserver_ = İnformation(option)
                nameserver_ = nameserver_.nameserver_lookup()
                print(nameserver_)
                input("▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")
                clear()

            elif option == "03":
                clear()
                banner_traceroute = tracert_banner.banner__traceroute()
                option = input("Enter İp / Host : ")
                traceroute = İnformation(option)
                traceroute = traceroute.traceroute_lookup()
                print(traceroute)
                input("▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")
                clear()

            elif option == "04":
                clear()
                banner_fake_nmap =  fake_nmap_banner.banner__nmap()
                nmap_options = options_nmap()
                nmap = input("Enter Options Nmap : ")

                if nmap == "99":
                    break
                else:
                    if nmap == "1":
                        option = input("Enter İp / Host : ")
                        nmap_dns_brute = NmapFunction(option)
                        nmap_dns_brute = nmap_dns_brute.dns_nmap()
                        input("▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")
                        clear()
                    elif nmap == "2":
                        option = input("Enter İp / Host : ")
                        nmap_arp = NmapFunction(option)
                        nmap_arp = nmap_arp.tcp_scanner_nmap()
                        input("▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")
                        clear()


            elif option == "05":
                clear()
                banner_proxy = proxy_banner.banner__proxy()
                proxy_options = options_proxy()
                proxy = input("Enter Options Proxy : ")
                if proxy == "99":
                    break
                else:
                    if proxy == "1":
                        f = open("scrape-proxy-socks5.txt","w")
                        try:
                            scrape_proxy = get_proxy_scrape()
                            f.write(scrape_proxy)
                            sys.stdout.write(str(colored.blue("[+ Successfully Proxy ]\n[+ Proxy Added scrape-proxy-socks5.txt ]")))
                            sys.stdout.flush()
                            f.close()
                            input("\nPress Enter Options")

                        except Exception as ex:
                            f.close()
                            sys.stdout.write(str(colored.green("[ + Website !!! Not Found ]")))
                            sys.stdout.flush()
                            print(ex)
                            sys.exit()

                    elif proxy == "2":
                        f = open("proxy-list-web-socks5-txt","w")
                        try:
                            proxy_list_web = get_proxy_proxy_list()
                            f.write(proxy_list_web)
                            sys.stdout.write(str(colored.blue("[+ Successfully Proxy ]\n[+ Proxy Added proxy-list-web-socks5-txt ]")))
                            sys.stdout.flush()
                            f.close()
                            input("\nPress Enter Options")
                        
                        except Exception as ex:
                            f.close()
                            sys.stdout.write(str(colored.green("[ + Website !!! Not Found ]")))
                            sys.stdout.flush()
                            print(ex)
                            sys.exit()

                    elif proxy == "3":
                        f = open("scrape-proxy-socks4.txt","w")
                        try:
                            scrape_proxy_socks4 = get_proxy_scrape_socks4()
                            f.write(scrape_proxy_socks4)
                            sys.stdout.write(str(colored.blue("[+ Successfully Proxy ]\n[+ Proxy Added scrape-Proxy-socks4.txt ]")))
                            sys.stdout.flush()
                            f.close()
                            input("\nPress Enter Options")

                        except Exception as ex:
                            f.close()
                            sys.stdout.write(str(colored.green("[ + Website !!! Not Found ]")))
                            sys.stdout.flush()
                            print(ex)
                            sys.exit()


                    elif proxy == "4":
                        f = open("proxy-list-web-socks4-txt","w")
                        try:
                            proxy_list_web_socks4 = get_proxy_proxy_list_socks4()
                            f.write(proxy_list_web_socks4)
                            sys.stdout.write(str(colored.blue("[+ Successfully Proxy ]\n[+ Proxy Added proxy-list-web-socks4-txt ]")))
                            sys.stdout.flush()
                            f.close()
                            input("\nPress Enter Options")
                        
                        except Exception as ex:
                            f.close()
                            sys.stdout.write(str(colored.green("[ + Website !!! Not Found ]")))
                            sys.stdout.flush()
                            print(ex)
                            sys.exit()


            
            elif option == "06":
                clear()
                banner_layer_seven = layer_seven_banner.banner__layer_seven()
                option = input("Enter İp / Address : ")

            
            elif option == "07":
                clear()
                banner_subdomain = subdomain_banner.banner__subdomain()
                option = input("Enter İp / Host : ")
                selenium_ = Seleniumİnformation(option)
                selenium_.selenium_subdomain()
                time.sleep(2)
                input("\n▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")

            elif option == "08":
                clear()
                banner_waf = waf_banner.banner__waf()
                option = input("Enter İp / Host [ + http / https ]  : ")
                print(colored.green("""[ + Please Wait 10 Second Loading .... ]"""))
                selenium_waf = Seleniumİnformation(option)
                selenium_waf.selenium_wafchecker()
                input("\n▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")
            
            elif option == "09":
                clear()
                banner_social = social_banner.banner__social()
                option = input("Enter Social Media Address : ")
                social_start = SocialMedia(option)
                social_start.facebook()
                social_start.instagram()
                social_start.github()
                social_start.twitter()
                social_start.youtube()
                input("\n▬▬▬▬▬▬▬▬ Press Enter Options ▬▬▬▬▬▬▬▬\n")


    except KeyboardInterrupt:
        sys.exit()
    except Exception as ex:
        print(ex)
        sys.exit()
