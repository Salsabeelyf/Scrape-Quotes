import requests

url = "http://quotes.toscrape.com/"

response = requests.get(url)

print(response.status_code)
print(response.headers)

content = response.content

print(content.decode("utf-8"))