import requests


url="https://pay.thinkerx.com/cms/login/in"
body= {
            "account": "nihaoping",
            "password": "0c98adac760bd840c30d2d143fbb38a4",
            "loading": "true"
        }

header = {"Content-Type":"multipart/form-data"}

response = requests.post(url, params=body)

print(response.text)