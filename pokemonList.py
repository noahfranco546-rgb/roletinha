
import random


class PokemonList:
    def __init__(self, listUsers, listElements):
        self.listUsers = listUsers
        self.listElements = listElements
        self.listSortedUsers = ()


    def doorPrizePokemon(self):
        if len(self.listUsers) > 1:
            if len(self.listElements) > 1:
                
                sorteadoElements = random.choice(self.listElements)
                sorteadoUsers = random.choice(self.listUsers)
                self.listSortedUsers.append((sorteadoUsers, sorteadoElements))
                self.listElements.remove(sorteadoElements)
                self.listUsers.remove(sorteadoUsers)
            else:
                return "FAÇA O L, IMEDIATAMENTE"