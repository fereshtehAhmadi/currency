import requests


url = 'https://api.exchangerate.host/latest'


response = requests.get(url)
data = response.json()

USD = data['rates']['USD']

TOMAN = USD * 3794894.679351561
print(f"{TOMAN} toman")

			