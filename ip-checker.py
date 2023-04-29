import requests
import ipaddress
import json
import sys

def check_input_ip():
    ip_address=input("Enter a valid IP:")
    try:
        ip = ipaddress.ip_address(ip_address)
        if ip.is_private:
            print(f"{ip_address} is a private IP address.\n and is only used in internal network environments")
            sys.exit()
        else:
            print(f"{ip_address} is a public IP address.")
    except ValueError:
        print(f"{ip_address} is not a valid IP address.")



check_input_ip()
