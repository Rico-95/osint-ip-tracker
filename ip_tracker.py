import requests

def track_ip(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(f"\nIP Info for {ip_address}")
        print(f"IP: {data.get('ip')}")
        print(f"City: {data.get('city')}")
        print(f"Region: {data.get('region')}")
        print(f"Country: {data.get('country')}")
        print(f"Org: {data.get('org')}")
        print(f"Location: {data.get('loc')}")
    else:
        print("Error fetching data. Check the IP or your internet connection.")

if __name__ == "__main__":
    ip = input("Enter an IP address to track: ")
    track_ip(ip)
