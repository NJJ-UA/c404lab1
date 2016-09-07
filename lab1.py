import requests

response = requests.post('http://ccid-eddieantonio.rhcloud.com/jni1')
print(response.status_code)