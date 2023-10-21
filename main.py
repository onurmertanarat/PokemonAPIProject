import requests


def main():
    rsp = requests.get('http://pokeapi.co/api/v2/pokemon/1/')
    if rsp.status_code == 200:
        json_rsp = rsp.json()
        poke_name = json_rsp['name']
        print(poke_name)


main()
