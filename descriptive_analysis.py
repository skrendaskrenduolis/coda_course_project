import matplotlib.pyplot as plt
import pycodamath as coda
import pandas as pd
from load_data import pokemon_data, colors


if __name__ == "__main__":
    print("hello world")
    print(pokemon_data)
    # primary_types = set(pokemon_data["Type 1"].unique())
    # secondary_types = set(pokemon_data["Type 2"].unique())
    # print(primary_types)
    # print(secondary_types)
    # print(primary_types.difference(secondary_types))
    # print(secondary_types.difference(primary_types))
    # print(len(primary_types.union(secondary_types)))


    pokemon_data_type_grouped = pokemon_data.groupby(["Type 1", "Type 2"]).size().unstack(fill_value=0)
    pokemon_data_type_grouped.plot(kind="bar", stacked=True, color=[colors[col] for col in pokemon_data_type_grouped.columns])
    plt.xlabel('Type 1')
    plt.ylabel('Count')
    plt.title('Stacked Bar Chart of Pokemon Type 1 stratified by Type 2')
    plt.show()


    pokemon_data_type_grouped_2 = pokemon_data.groupby(["Type 2", "Type 1"]).size().unstack(fill_value=0)
    pokemon_data_type_grouped_2.plot(kind="bar", stacked=True, color=[colors[col] for col in pokemon_data_type_grouped_2.columns])
    plt.xlabel('Type 2')
    plt.ylabel('Count')
    plt.title('Stacked Bar Chart of Pokemon Type 1 stratified by Type 2')
    plt.show()

    covariates = pokemon_data.iloc[:, 0:3]
    closed_abilities = pokemon_data.iloc[:, 3:].coda.closure(100)
    pokemon_data_closed = pd.concat([covariates, closed_abilities], axis=1)
    print(pokemon_data_closed)

    # Step 1: Filter rows based on a specific value in column 1

# for specific_value in pokemon_data_closed["Type 1"].unique():

#     #specific_value = "Dragon"
#     filtered_pokemon_data_closed = pokemon_data_closed[pokemon_data_closed['Type 1'] == specific_value]

#     # Step 2: Create a stacked bar plot with columns 3 to 8
#     # stacked_data = filtered_pokemon_data_closed.iloc[:, 3:9]

#     filtered_pokemon_data_closed.plot(kind='bar', stacked=True, x='Name', y =["HP", "Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed"] )
#     plt.xlabel('Pokemon name')
#     plt.ylabel('Relative percentage of stats')
#     plt.title(f'{specific_value} type relative percentage of stats')
#     plt.show()

    