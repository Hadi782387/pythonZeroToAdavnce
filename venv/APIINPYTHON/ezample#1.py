# how to connect API
import requests

base_url = "https://pokeapi.co/api/v2/"

def getPokemonInfo(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code==200:
        pokeinfo = response.json()
        return pokeinfo
    else:
        print("data doesnt found:")
pokemon_name = "pikachu"
pokedata = getPokemonInfo(pokemon_name)
if pokedata:
    print(f"Name: ",pokedata["name"])
    print(f"weight: ",pokedata["weight"])
    print(f"height: ",pokedata["height"])
    print(f"id: ",pokedata["id"])


