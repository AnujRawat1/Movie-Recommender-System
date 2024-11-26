import requests

url1 = "https://api.themoviedb.org/3/movie/285?api_key=2daa7ffee94a387ade64b767b27380a9&language=en-US"
url2 = "https://catfact.ninja/fact"

response = requests.get(url1, timeout=7)

data = response.json()

print(data)
