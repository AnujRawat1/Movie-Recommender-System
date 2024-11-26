import requests

url = "https://api.themoviedb.org/3/movie/19995?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyZGFhN2ZmZWU5NGEzODdhZGU2NGI3NjdiMjczODBhOSIsIm5iZiI6MTczMTEzMjcxNS44Mzg2Niwic3ViIjoiNjcyZWViOGFhYzAxNDlhNjc4YjkwZTRjIiwic2NvcGVzIjpbImFwaV9yZWFkIl0sInZlcnNpb24iOjF9.LcbUAt8pBnpYuThoFofIIRYfbcYuRIJVCdYrnYHqZtc"
}

response = requests.get(url, headers=headers,timeout=5)

print(response.text)

import requests

url = "https://api.themoviedb.org/3/movie/19995?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer 2daa7ffee94a387ade64b767b27380a9"
}

response = requests.get(url, headers=headers)

print(response.text)