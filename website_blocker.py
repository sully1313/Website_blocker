# to run on OSX use the command sudo python3 website_blocker.py

import time
from datetime import datetime as dt

hosts_path="/etc/hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "facebook.com"]


while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() and dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):
        print("...Working hours")
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write("%s %s\n"% (redirect, website))
    else:
        with open(hosts_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("...Fun Hours")
    time.sleep(5)
