""" import requests

def getPoke(poke):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{poke.lower()}")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }

pokemon = getPoke("Bulbasaur")
print(pokemon) """

import requests

e1=input("What measurement system are you using. Ex. Time")
e2=input("What unit are you converting from. Ex. Second")
e3=input("What unit are you converting to. Ex. Day")
e4=input("How many units do you want to convert? Ex. 8748989638")
def units(type,unit,unit2,quantity):
    
    response = requests.get(f"https://api.unusualunits.com/convert/{type.lower()}/{unit.lower()}/{unit2.lower()}/{quantity}")
    if response.status_code !=200:
        print("Error")
        return None
    
    data=response.json()
    return {
        "Value":data["result"]
    }
horastodias=units(e1,e2,e3,e4)
print(horastodias)
    