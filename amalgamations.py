import matplotlib.pyplot as plt
import pycodamath as coda
import pandas as pd
from load_data import pokemon_data, colors
from custom_ternary import ternary


print(pokemon_data)
covariates = pokemon_data.iloc[:, 0:3]
    #closed_abilities = pokemon_data.iloc[:, 3:].coda.closure(100)
pokemon_data["Tot. Atk"] = pokemon_data[["Attack", "Sp. Atk"]].sum(axis=1, numeric_only=True)
pokemon_data["Tot. Def"] = pokemon_data[["Defense", "Sp. Def"]].sum(axis=1, numeric_only=True)
pokemon_data["Tot. Special"] = pokemon_data[["Sp. Atk", "Sp. Def"]].sum(axis=1, numeric_only=True)
pokemon_data["Tot. Physical"] = pokemon_data[["Attack", "Defense"]].sum(axis=1, numeric_only=True)



### PRIMARY TYPE
## HP 

special_physical_split = pokemon_data[["HP", "Tot. Special", "Tot. Physical"]].coda.closure(100)
atk_def_split = pokemon_data[["HP", "Tot. Atk", "Tot. Def"]].coda.closure(100)

special_physical_split = pd.concat([covariates, special_physical_split], axis=1)
atk_def_split = pd.concat([covariates, atk_def_split], axis=1)

special_physical_split["color"] = special_physical_split["Type 1"].map(colors)
print(special_physical_split)
#print(atk_def_split)
print(colors)

ternary(special_physical_split[["HP", "Tot. Special", "Tot. Physical"]], descr=special_physical_split["Type 1"], colors_dict=colors)
plt.legend()
plt.show()

ternary(atk_def_split[["HP", "Tot. Atk", "Tot. Def"]], descr=atk_def_split["Type 1"], colors_dict=colors)
plt.legend()
plt.show()



## SPEED

special_physical_split = pokemon_data[["Speed", "Tot. Special", "Tot. Physical"]].coda.closure(100)
atk_def_split = pokemon_data[["Speed", "Tot. Atk", "Tot. Def"]].coda.closure(100)
special_physical_split = pd.concat([covariates, special_physical_split], axis=1)
atk_def_split = pd.concat([covariates, atk_def_split], axis=1)

ternary(special_physical_split[["Speed", "Tot. Special", "Tot. Physical"]], descr=special_physical_split["Type 1"], colors_dict=colors)
plt.legend()
plt.show()

ternary(atk_def_split[["Speed", "Tot. Atk", "Tot. Def"]], descr=atk_def_split["Type 1"], colors_dict=colors)
plt.legend()
plt.show()



###### SECONDARY TYPE
## HP 

special_physical_split = pokemon_data[["HP", "Tot. Special", "Tot. Physical"]].coda.closure(100)
atk_def_split = pokemon_data[["HP", "Tot. Atk", "Tot. Def"]].coda.closure(100)

special_physical_split = pd.concat([covariates, special_physical_split], axis=1)
atk_def_split = pd.concat([covariates, atk_def_split], axis=1)

special_physical_split["color"] = special_physical_split["Type 2"].map(colors)
print(special_physical_split)
#print(atk_def_split)
print(colors)

ternary(special_physical_split[["HP", "Tot. Special", "Tot. Physical"]], descr=special_physical_split["Type 2"], colors_dict=colors)
plt.legend()
plt.show()

ternary(atk_def_split[["HP", "Tot. Atk", "Tot. Def"]], descr=atk_def_split["Type 2"], colors_dict=colors)
plt.legend()
plt.show()



## SPEED

special_physical_split = pokemon_data[["Speed", "Tot. Special", "Tot. Physical"]].coda.closure(100)
atk_def_split = pokemon_data[["Speed", "Tot. Atk", "Tot. Def"]].coda.closure(100)
special_physical_split = pd.concat([covariates, special_physical_split], axis=1)
atk_def_split = pd.concat([covariates, atk_def_split], axis=1)

ternary(special_physical_split[["Speed", "Tot. Special", "Tot. Physical"]], descr=special_physical_split["Type 2"], colors_dict=colors)
plt.legend()
plt.show()

ternary(atk_def_split[["Speed", "Tot. Atk", "Tot. Def"]], descr=atk_def_split["Type 2"], colors_dict=colors)
plt.legend()
plt.show()
