from bs4 import BeautifulSoup
import requests


user = input("enter how much you have:  ")
url = 'https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1'


response = requests.get(url)
html_doc = response.text


soup = BeautifulSoup(html_doc, 'html.parser')

td = soup.find('td').contents[0]
td = td.split(",")
td = int(td[0]+td[1])
price = int(user)*td


print(price)
			