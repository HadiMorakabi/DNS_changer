# DNS_changer
a python project for changing DNS settings in windows
<br>changing DNS settings in Windows is a tedious proceess and needs 5-9 clicks + typing DNS server ip address. so I wrote this python Script to make it easy.
# How to use:
it is recommended to make this python script to a .exe file. to do this you should have python installed on your system. then install pyinstaller package by running this command in cmd:
<br>pip install pyinstaller
then change your current directory to where this repo is extracted(your_path/DNS_changer), then run this:
<br>pyinstaller --icon dns.ico dns.py
<br>then you will two folders and one file: bulid, dist and dns.spec
<br>go to dist/dns and you will find dns.exe
# Notice
don't forget to run the .exe file with administrator permission.
<br>enjoy!
# Latest changes
added a new button to see the current dns ip address
.
.
.
