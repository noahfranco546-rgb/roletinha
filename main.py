import userList
import pokemonList

class Main():
    def __init__(self):
        self
        
        
    listUsers = userList.UserList(["Gabriel - Hardware (Fullcond)",
                      "Vitor - Mobile (Fullcond)",
                      "Gabriel - AWS(careca) Infra",
                      "Enzo - infra ",
                      "Thiago - (Fullcond)",
                      "Gui - (Fullcond)",
                      "João Jorge - Infra",
                      "Lucas Vieria (capas) - (Fullcond)",
                      "Noah - (Fullcond)",
                      "Vitor santos - (Fullcond)"])
    
    listElementos = pokemonList.PokemonList(["Aço (Steel)",
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
                    "Sombrio (Dark)" ,
                    "Terrestre (Ground)",
                    "Venenoso (Poison)",
                    "Fantasma (Ghost)"
                    "Voador (Flying) "
])
    
    
print(Main.listUsers.getUsers())
print(Main.listElementos.list)
    
    
        
   
