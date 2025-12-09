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

import tkinter as tk

window=tk.Tk()
window.title("Converter")
window.geometry("500x600")
window.resizable(False,False) 

prompt1 = tk.Label(window, text="Type your measurement system below:", font=("Arial", 16))
prompt1.pack(pady=10) 
entry1 = tk.Entry(window, font=("Arial", 14), width=30)
entry1.pack(pady=5)
result_label1 = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label1.pack(pady=15)

prompt2 = tk.Label(window, text="Type your starting unit:", font=("Arial", 16))
prompt2.pack(pady=10) 
entry2 = tk.Entry(window, font=("Arial", 14), width=30)
entry2.pack(pady=5)
result_label2 = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label2.pack(pady=15)

prompt3 = tk.Label(window, text="Type your unit to convert to:", font=("Arial", 16))
prompt3.pack(pady=10) 
entry3 = tk.Entry(window, font=("Arial", 14), width=30)
entry3.pack(pady=5)
result_label3 = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label3.pack(pady=15)

prompt4 = tk.Label(window, text="Type the number of your starting unit:", font=("Arial", 16))
prompt4.pack(pady=10) 
entry4 = tk.Entry(window, font=("Arial", 14), width=30)
entry4.pack(pady=5)
result_label4 = tk.Label(window, text="", font=("Arial", 14, "bold"), fg="blue")
result_label4.pack(pady=15)

window.mainloop()

def units(type,unit,unit2,quantity):
    
    response = requests.get(f"https://api.unusualunits.com/convert/{type.lower()}/{unit.lower()}/{unit2.lower()}/{quantity}")
    if response.status_code !=200:
        print("Error")
        return None
    
    data=response.json()
    return {
    "Value":data["result"]
        }


