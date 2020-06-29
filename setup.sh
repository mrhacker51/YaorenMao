#!/bin/bash

clear

echo "
██╗   ██╗ █████╗  ██████╗ ██████╗ ███████╗███╗   ██╗███╗   ███╗ █████╗  ██████╗ 
╚██╗ ██╔╝██╔══██╗██╔═══██╗██╔══██╗██╔════╝████╗  ██║████╗ ████║██╔══██╗██╔═══██╗
 ╚████╔╝ ███████║██║   ██║██████╔╝█████╗  ██╔██╗ ██║██╔████╔██║███████║██║   ██║
  ╚██╔╝  ██╔══██║██║   ██║██╔══██╗██╔══╝  ██║╚██╗██║██║╚██╔╝██║██╔══██║██║   ██║
   ██║   ██║  ██║╚██████╔╝██║  ██║███████╗██║ ╚████║██║ ╚═╝ ██║██║  ██║╚██████╔╝
   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝ 
                                                                                
██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██╗     ███████╗██████╗           
██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗          
██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝          
██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗          
██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║          
╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
";


apt-get update
apt-get install python-pip -y 
apt-get install python3-pip -y
apt-get install python-setuptools -y
apt-get install python3-setuptools -y
pip3 install clint
pip3 install colored
pip install selenium
pip3 install selenium
pip3 install bs4
pip3 install requests

wget https://github.com/mozilla/geckodriver/releases/download/v0.26.0/geckodriver-v0.26.0-linux64.tar.gz
tar -xvf geckodriver-v0.26.0-linux64.tar.gz
rm -rf geckodriver-v0.26.0-linux64.tar.gz

wget https://ftp.mozilla.org/pub/firefox/releases/77.0.1/linux-x86_64/en-US/firefox-77.0.1.tar.bz2
tar -xvf firefox-77.0.1.tar.bz2
rm -rf firefox-77.0.1.tar.bz2
