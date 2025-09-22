import requests

API_BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_info(pokemon: str):
    url = f"{API_BASE_URL}/pokemon/{pokemon.lower()}"
    response = requests.get(url)

    return response.json()


def main() -> None:
    pikachu = get_pokemon_info("Pikachu")
    #bulbasaur = get_pokemon_info("Bulbasaur")

    print(pikachu)
    #print(bulbasaur)


if __name__ == '__main__':
    main()