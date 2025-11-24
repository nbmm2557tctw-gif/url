import requests, json, os

config = json.load(open("config.json"))
HEADERS = {
    "Authorization": f"Bearer {config['CF_API_TOKEN']}",
    "Content-Type": "application/json"
}

def get_ip():
    return requests.get("https://api.ipify.org").text

def get_record_id():
    url = f"https://api.cloudflare.com/client/v4/zones/{config['ZONE_ID']}/dns_records"
    r = requests.get(url, headers=HEADERS, params={"type": config["RECORD_TYPE"], "name": config["RECORD_NAME"]}).json()
    return r["result"][0]["id"]

def update_dns(ip):
    record_id = get_record_id()
    url = f"https://api.cloudflare.com/client/v4/zones/{config['ZONE_ID']}/dns_records/{record_id}"
    data = {
        "type": config["RECORD_TYPE"],
        "name": config["RECORD_NAME"],
        "content": ip,
        "ttl": 120,
        "proxied": True
    }
    r = requests.put(url, headers=HEADERS, json=data).json()
    if r["success"]:
        print(f"更新成功: {config['RECORD_NAME']} -> {ip}")
    else:
        print("更新失敗", r)

if __name__ == "__main__":
    ip = get_ip()
    update_dns(ip)
