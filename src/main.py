'''
    Created by jrkinch
    Project for scrapping pokemon names.
    #pylint: disable=line-too-long.
    #Data source url is long.
    Data Source: "https://m.bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
'''
from pokemon_list.pokemon_list import PokemonList


if __name__ == "__main__":
    #init class.
    pl = PokemonList()

    #checks for data file and gets latest data.
    pl.check_file_and_get_latest()
