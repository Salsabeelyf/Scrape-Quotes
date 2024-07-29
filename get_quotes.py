from urllib.request import urlopen

url = "http://quotes.toscrape.com/"

with urlopen(url) as response:
    print(response.status)
    content = response.read()
    print(content.decode("utf-8"))