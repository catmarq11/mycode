import requests

url= "http://10.0.0.80:3000/data"

response= requests.get(url)

response= response.json()

for joke in response["jokes"]:
    print(f"""
        {joke["setup"]}
        {joke["punchline"]}
    """)
