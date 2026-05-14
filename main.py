from userList import UserList
from pokemonList import PokemonList


class Main:
    def __init__(self):
        self.listUsers = UserList([
            "Gabriel - Hardware (Fullcond)",
            "Vitor - Mobile (Fullcond)",
            "Gabriel - AWS(careca) Infra",
            "Enzo - infra ",
            "Thiago - (Fullcond)",
            "Gui - (Fullcond)",
            "João Jorge - Infra",
            "Lucas Vieria (capas) - (Fullcond)",
            "Noah - (Fullcond)",
            "Vitor santos - (Fullcond)"
        ])

        self.listElementos = PokemonList([
            "Aço (Steel)",
            "Água (Water)",
            "Dragão (Dragon)",
            "Elétrico (Electric)",
            "Fada (Fairy)",
            "Fogo (Fire)",
            "Gelo (Ice)",
            "Inseto (Bug)",
            "Lutador (Fighting)",
            "Normal",
            "Planta (Grass)",
            "Psíquico (Psychic)",
            "Pedra (Rock)",
            "Sombrio (Dark)",
            "Terrestre (Ground)",
            "Venenoso (Poison)",
            "Fantasma (Ghost)",
            "Voador (Flying)"
        ])


if __name__ == "__main__":
    app = Main()
    # exibe listas
    print(app.listUsers.list)
    print(app.listElementos.list)
    # exemplo: sorteio de usuário e de pokémon
    print('Sorteado usuário:', app.listUsers.doorPrize())
    print('Sorteado elemento:', app.listElementos.doorPrizePokemon())




