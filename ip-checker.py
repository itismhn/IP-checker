import requests
import ipaddress
import json
import sys

abusedIP_api_key = "61fea5fdc3f8cf218003031b37915c1ab8e909ce83986cff1a0d4928babe7f04fb32b49f7cf32336"

def check_input_ip():
    ip_address=input("Enter a valid IP:")
    try:
        ip = ipaddress.ip_address(ip_address)
        if ip.is_private:
            print(f"{ip_address} is a private IP address.\n and is only used in internal network environments")
            sys.exit()
        else:
            print(f"{ip_address} is a public IP address.")
            abused_ip(ip_address)
    except ValueError:
        print(f"{ip_address} is not a valid IP address.")

def abused_ip(ip_address):
    url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}&maxAgeInDays=90"
    headers = {
    "Key": abusedIP_api_key,
    "Accept": "application/json"
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = json.loads(response.content.decode("utf-8"))
        print(f"The IP address {ip_address} -  confidence score of {data['data']['abuseConfidenceScore']}.")
        print("IP details:")
        print(f"IP address: {data['data']['ipAddress']}")
        print(f"Abuse confidence score: {data['data']['abuseConfidenceScore']}")
        print(f"Number of reports: {data['data']['totalReports']}")
        print(f"Last reported: {data['data']['lastReportedAt']}")
        print(f"ISP: {data['data']['isp']}")
        print(f"Country: {data['data']['countryCode']}")

    else:
        print(f"An error occurred while checking the IP address: {response.status_code}")



check_input_ip()
