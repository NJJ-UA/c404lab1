import requests

response = requests.get('https://github.com/NJJ-UA/c404lab1/raw/master/lab1.py')
print(response.text)