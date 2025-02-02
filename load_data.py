import numpy as np
import pandas as pd

pokemon_data = pd.read_csv("Pokemon_gen1.csv", sep=";", index_col='#')
pokemon_data.fillna({"Type 2": "Monotype"}, inplace=True)
print(pokemon_data["Type 1"].unique())
print(pokemon_data["Type 2"].unique())

colors = {"Grass": "green", "Fire": "orange", "Water": "#069AF3",
            "Bug": "lime", "Normal": "black", "Poison": "purple",
            "Electric": "yellow", "Ground":"sienna", "Fairy": "fuchsia",
            "Fighting": "red", "Psychic": "pink", "Rock": "tan",
            "Ghost": "#C79FEF", "Ice": "cyan", "Dragon": "blue",
            "Steel": "#06C2AC", "Flying": "#C1F80A", "Monotype":"grey"} #, usecols=["x1", "x2", "x3"])
print(pokemon_data)

