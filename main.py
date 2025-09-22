import requests

API_BASE_URL = "https://pokeapi.co/api/v2"

def get_pokemon_info(pokemon: str):
    url = f"{API_BASE_URL}/pokemon/{pokemon.lower()}"
    response = requests.get(url)

    return response.json()


def main() -> None:
    print("PokeAPI")
    pikachu = get_pokemon_info("Pikachu")
    print(pikachu)


if __name__ == '__main__':
    main()