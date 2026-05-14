
import random


class PokemonList:
    def __init__(self, list):
        self.list = list

    def doorPrizePokemon(self):
        if len(self.list) > 1:
            sorteado = random.choice(self.list)
            self.list.remove(sorteado)
            return sorteado
        else:
            return "FAÇA O L, IMEDIATAMENTE"