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

constantinople=True
while constantinople==True:

    import tkinter as tk

    window=tk.Tk()
    window.title("Converter")
    window.geometry("640x400")
    window.resizable(False,False) 
    prompt = tk.Label(window, text="Type your measurement system below:", font=("Arial", 16))
    prompt.pack(pady=10) 
    entry = tk.Entry(window, font=("Arial", 14), width=30)
    entry.pack(pady=5)
    result_label = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
    result_label.pack(pady=15)

    def units(type,unit,unit2,quantity):
    
        response = requests.get(f"https://api.unusualunits.com/convert/{type.lower()}/{unit.lower()}/{unit2.lower()}/{quantity}")
        if response.status_code !=200:
            print("Error")
            return None
    
        data=response.json()
        return {
        "Value":data["result"]
        }

    horastodias=units(result_label.text(), )
    print(horastodias)
