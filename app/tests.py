from django.test import TestCase
import requests

url = 'http://127.0.0.1:8000/list/student'
token = "c4a6b64f21e604df28dc31a3607698f38217d2de"

headers = {'Authorization': f'Token {token}'}
response = requests.get(url, headers=headers)

# Javobni tekshirish
if response.status_code == 200:
    print('Serverdan muvaffaqiyatli javob qaytdi.')
    print(response.json())
else:
    print('Serverdan xato javob qaytdi.')