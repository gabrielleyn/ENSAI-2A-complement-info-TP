from business_object.pokemon.abstract_pokemon import Pokemon


class AllRounderPokemon(Pokemon):
    def __init__(self):
        super().__init__()

    def get_pokemon_all_rounder_coef(self) -> float:
        """
        Commentaire
        """
        multiplier = 1 + (self.sp_atk_current + self.sp_def_current) / 200
        return multiplier
