import requests

with open("common.txt","r") as file:
    f=file.read().splitlines()
    
url = "http://www.vulnweb.com/FUZZ"

for n in f:
    name = url.replace("FUZZ", n)
    reponse = requests.get(name, timeout=5)
    print(name)
    if reponse.status_code== 200:
        print(f"200 {name}")
        break
    
