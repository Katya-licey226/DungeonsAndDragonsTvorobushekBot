def giga_get (ques):
        import requests
            import json
            import time
                
            url_get = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
            response = None
            payload='scope=GIGACHAT_API_PERS'
            headers = {
              'Content-Type': 'application/x-www-form-urlencoded',
              'Accept': 'application/json',
              'RqUID': '7079cac6-f5ca-4549-810a-09fb3b00244c',
              'Authorization': 'Basic YTRmODNiYzctNzdjMC00MGRlLTg1NzktNTBiNzdjNzEyMmU1OjcwNzljYWM2LWY1Y2EtNDU0OS04MTBhLTA5ZmIzYjAwMjQ0Yw=='
            }

            response = requests.request("POST", url_get, headers=headers, data=payload, verify=False)
            date = response.json()
            token = date['access_token']
            print(token)
        
            url_responce = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"

            payload = json.dumps({
              "model": "GigaChat",
              "messages": [
                {
                  "role": "user",
                  "content": ques
                }
              ],
              "n": 1,
              "stream": False,
              "update_interval": 0
            })
            headers = {
              'Content-Type': 'application/json',
              'Accept': 'application/json',
              'Authorization': f'Bearer {token}'
            }

            response = requests.request("POST", url_responce, headers=headers, data=payload, verify=False)
            context = response.json()
            response_in_context = context['choices'][0]['message']['content']
            print (response_in_context)
            return response_in_context
