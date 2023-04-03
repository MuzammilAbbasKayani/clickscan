from sys import argv
import time
import os
import urllib.request
import requests
import threading
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
print("==========ClickScan============")

script, filename = argv
print ("Scan started")
with open(filename, "r") as f:
    subdomains = f.readlines()
      
def check_subdomain(subdomain):
    newsubdomain = "http://%s" % subdomain.strip()
 
    try:
        response = requests.get(newsubdomain, timeout=(10, 60),allow_redirects=True, verify=False)
        headers = response.headers
        if 'X-Frame-Options' not in headers:
            print(f"{subdomain.strip()} is vulnerable to Clickjacking")
        else:
            print(f"{subdomain.strip()} is not vulnerable to Clickjacking")
    except (requests.exceptions.Timeout, requests.exceptions.RequestException):
        print(f"{subdomain.strip()} domain is not alive")
 
threads = []
for subdomain in subdomains:
    thread = threading.Thread(target=check_subdomain, args=(subdomain,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print("Scan completed")       
    
