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

def abused_ip():
    abused_api_key = "61fea5fdc3f8cf218003031b37915c1ab8e909ce83986cff1a0d4928babe7f04fb32b49f7cf32336"
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}&maxAgeInDays=90"


check_input_ip()
