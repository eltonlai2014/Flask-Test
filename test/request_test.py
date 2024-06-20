import requests

response = requests.get("http://books.toscrape.com")
if not response.ok:
    print(response.status_code)
    print(response.text)
    pass
print(response.status_code)
print(response.text)