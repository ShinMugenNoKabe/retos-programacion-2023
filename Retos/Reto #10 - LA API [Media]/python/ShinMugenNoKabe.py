import requests


def make_petition() -> dict:
    response = requests.get("https://pokeapi.co/api/v2/pokemon/meowth")
    return response.json()


if __name__ == "__main__":
    print(make_petition())