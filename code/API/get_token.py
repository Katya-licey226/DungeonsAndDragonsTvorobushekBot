import requests

url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

payload='scope=GIGACHAT_API_PERS'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json',
  'RqUID': '7079cac6-f5ca-4549-810a-09fb3b00244c',
  'Authorization': 'Basic YTRmODNiYzctNzdjMC00MGRlLTg1NzktNTBiNzdjNzEyMmU1OjcwNzljYWM2LWY1Y2EtNDU0OS04MTBhLTA5ZmIzYjAwMjQ0Yw=='
}

response = requests.request("POST", url, headers=headers, data=payload, verify=False)

print(response.text)