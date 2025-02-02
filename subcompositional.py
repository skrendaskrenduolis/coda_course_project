import matplotlib.pyplot as plt
import pycodamath as coda
import numpy as np
import pandas as pd
import scipy.stats as ss
import itertools
from load_data import pokemon_data, colors
from custom_ternary import ternary

#spdef speed hp
def closure_np(input, k):
    input_sum = np.sum(input)
    output = input * k/input_sum
    return output



attributes = ["Attack", "Defense", "Sp. Atk", "Sp. Def", "Speed", "HP"]
unique_combinations = list(itertools.combinations(attributes, 3))
unique_combinations = [list(comb) for comb in unique_combinations]

# One of the lines can be uncommented
pokemon_data = pokemon_data[pokemon_data["Type 1"].isin(["Fighting", "Psychic"])]
# pokemon_data = pokemon_data[pokemon_data["Type 2"].isin(["Flying", "Poison"])]

covariates = pokemon_data.iloc[:, 0:3]
for subcomposition in unique_combinations:
# [ ["Sp. Def", "HP", "Speed"],
#                         ["Sp. Atk", "Attack", "Defense"],
#                         ["Sp. Atk", "Attack", "Speed"],
#                         ["Sp. Atk", "Attack", "HP"],
#                         ["Sp. Atk", "HP", "Defense"]]:
    

    closed_abilities = pokemon_data[subcomposition].coda.closure(100)


    sample_center = ss.mstats.gmean(closed_abilities)
    sample_center = 100/np.sum(sample_center) * sample_center
    print(sample_center)

    var_matrix = closed_abilities.coda.varmatrix()

    print(var_matrix)

    total_variance = closed_abilities.coda.totvar()

    print(total_variance)



    clr = pow(closed_abilities/sample_center, 1./np.sqrt(total_variance)).coda.clr()
    s, e, l = coda.pca._svd(clr)
    # scale loadings with eigenvalues
    #l = np.inner(e*np.identity(3), l.T[0:3, 0:3])
    print(f"s\n{s}\n", f"e\n{e}\n", f"l\n{l}\n")\

    
    # plots
    # SCREE
    fig, ax = plt.subplots()
    myscree = coda.pca.scree_plot(axis = ax, eig_val = e)
    plt.show()


    ternary(closed_abilities[subcomposition], descr=covariates["Type 1"], colors_dict=colors)
    plt.legend()
    plt.show()

    ternary(closed_abilities[subcomposition], descr=covariates["Type 2"], colors_dict=colors)
    plt.legend()
    plt.show()

    # ## BIPLOT

    # mypca_type_1 = coda.pca.Biplot(closed_abilities)
    # mypca_type_1.removelabels()

    # mypca_type_1.plotloadings(cluster=True)
    # print(mypca_type_1.clusterlegend)
    # mypca_type_1.removelabels()
    # #mypca_type_1.removescores()
    # mypca_type_1.plotscores(group=covariates.iloc[:, 1], palette=colors, labels=covariates.iloc[:, 0])
    # #mypca_type_1.plotcentroids(group=covariates.iloc[:, 1], palette=colors)
    # #mypca_type_1.plotscorelabels(labels=covariates.iloc[:, 0])
    # #mypca_type_1.displaylegend(loc=1)
    # mypca_type_1.plotellipses(group=covariates.iloc[:, 1], palette=colors)
    # mypca_type_1.plotloadings(labels=subcomposition, cluster=False)
    # mypca_type_1.adjustloadinglabels()
    # mypca_type_1.displaylegend(loc=1)

    # plt.show()



    # mypca_type_2 = coda.pca.Biplot(closed_abilities)
    # mypca_type_2.removelabels()

    # mypca_type_2.plotloadings(cluster=True)
    # print(mypca_type_2.clusterlegend)
    # mypca_type_2.removelabels()
    # #mypca_type_2.removescores()
    # mypca_type_2.plotscores(group=covariates.iloc[:, 2], palette=colors, labels=covariates.iloc[:, 0])
    # #mypca_type_2.plotcentroids(group=covariates.iloc[:, 2], palette=colors)
    # #mypca_type_2.plotscorelabels(labels=covariates.iloc[:, 0])
    # #mypca_type_2.displaylegend(loc=1)
    # mypca_type_2.plotellipses(group=covariates.iloc[:, 2], palette=colors)
    # mypca_type_2.plotloadings(labels=subcomposition, cluster=False)
    # mypca_type_2.adjustloadinglabels()
    # mypca_type_2.displaylegend(loc=1)

    # plt.show()

  
    # #print(np.e**l.loc[["pc1"]].values.flatten())
    # points = []
    # gmean_values = closed_abilities.apply(ss.gmean, axis=1).values.flatten()
    # print(gmean_values)
    # edited_loadings = []
    # for loading in l.loc[["pc1"]].values.flatten():
    #     e_power = np.exp(loading)
    #     loading_scaled = pow(e_power,-1)
    #     edited_loadings.append(loading_scaled)
    # print(edited_loadings)

    # for value in gmean_values:
    #     edited_values = np.array(np.array(edited_loadings)*value)
    #     print(edited_values)
    #     points.append(closure_np(edited_values, 100))
    # print(points)




