from business_object.pokemon.abstract_pokemon import Pokemon


class DefenderPokemon(Pokemon):
    def __init__(self):
        super().__init__()

    def get_pokemon_defender_coef(self) -> float:
        """
        Commentaire
        """
        multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return multiplier
