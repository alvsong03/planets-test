import requests

response = requests.get(
    "https://www.loc.gov/resource/cph.3f05183",
    params={"fo": "json"},
)
data = response.json()
print(data)
