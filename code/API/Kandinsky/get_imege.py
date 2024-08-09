import json
import time
import base64
import requests


class Text2ImageAPI:

    def __init__(self, url, api_key, secret_key):
        self.URL = url
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        response = requests.get(self.URL + 'key/api/v1/models', headers=self.AUTH_HEADERS, verify=False)
        data = response.json()
        return data[0]['id']

    def generate(self, prompt, model, images=1, width=1024, height=1024):
        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }

        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + 'key/api/v1/text2image/run', headers=self.AUTH_HEADERS, files=data, verify=False)
        data = response.json()
        return data['uuid']

    def check_generation(self, request_id, attempts=10, delay=10):
        while attempts > 0:
            response = requests.get(self.URL + 'key/api/v1/text2image/status/' + request_id, headers=self.AUTH_HEADERS, verify=False)
            data = response.json()
            if data['status'] == 'DONE':
                return data['images']

            attempts -= 1
            time.sleep(delay)



api = Text2ImageAPI('https://api-key.fusionbrain.ai/', '5396A4AC1AF280BDDBB6EC121DC0E2E0', 'C0B9F36DA402CC6056237E81932B5EC5')
model_id = api.get_model()
uuid = api.generate("Sun in sky", model_id)
images = api.check_generation(uuid)
print(images)
image_base64 = images[0]
image_data = base64.b64decode(image_base64)
with open("image.jpg", "wb") as file:
    file.write(image_data)
#Не забудьте указать именно ваш YOUR_KEY и YOUR_SECRET.