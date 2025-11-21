<h1>pokemon-list</h1>
Project for scrapping Pokémon names.<br>

<h2>Description:</h2>

Project to extract pokemon list from website to an excel document.<br>
Data Source: "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"<br>
Wanted to do a webscrapping project using Selenium.<br>
&emsp;- Takes data from website and puts info into excel spreadsheet.<br>
&emsp;&emsp;- 'pokemon_output.xlsx' spreadsheet located in the 'pokemon_list/data' folder.<br>

pokemon_output.xlsx:<br>
&emsp;- Has five columns; 'Pokedex', 'Image', 'Name', 'Type1', 'Type2':<br>

| Pokedex | Image | Name | Type1 | Type2 |
| :----------: | :----------: | :----------: | :----------: | :----------: |
| Pokemon's number in the Pokedex. | URL location of PNG on web. | Pokemon's Name | Element type of Pokemon | Second element type of Pokemon, blank if None. |


<h2>Getting Started:</h2>

<h3>Installation:</h3>
1. Install the webdrivers for OS at "https://www.selenium.dev/downloads/".<br>
&emsp;- Project has setup for Chrome and Firefox webdrivers but other could be added.<br>

<br>
2. Clone the repo:

```console
git clone https://github.com/jrkinch/pokemon-list.git
```

<br>
3. Install python dependencies:

```console
pip install -r docs/requirements.txt
```
> [!TIP]
> Can also run the 'run_requirements.bat' from the 'scripts' folder.

<h3>Usage:</h3>
Steps to use in own project:<br>
1) Put the 'pokemon_list' folder in any project.<br>
2) Use <code>from pokemon_list.pokemon_list import PokemonList</code> in project.<br>
3) Init the class then use the 'check_file_and_get_latest' function from module.<br>
- Example:<br>

```python
from pokemon_list.pokemon_list import PokemonList
	
pl = PokemonList()
pl.check_file_and_get_latest()
```

> [!NOTE]
> Running <code>python main.py</code> from the 'src' folder checks if outdated and gets pokemon data.<br>
> ```python
>python main.py
> ```
