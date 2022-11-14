import requests
import random
import time

fuckq = int(9999999999)
for i in range(fuckq):  
  webhook = "PUT WEBHOOK HERE"
  name7 = "Flogster#5897"
  sex = requests.get("https://api.api-ninjas.com/v1/randomword")
  ani = sex.json()["word"] 
  domains = random.choice(["com","net"])
  message = (f"https://{ani}.{domains}")

  h = requests.post(webhook, json={"content": str(message), "name": str(name7), "avatar_url": "https://cdn.discordapp.com/attachments/933540730083872889/935019209652596736/01d8Ghah.jpg"})
  
  if h.status_code==204:  
    print(f"{h} - {message}")
  if h.status_code==429:  
    print("Rate Limited Cunt")
    time.sleep(1)
