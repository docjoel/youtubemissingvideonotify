import requests

r = requests.get("https://www.youtube.com/watch?v=ncPPgXKGsp4")
print(r.text)