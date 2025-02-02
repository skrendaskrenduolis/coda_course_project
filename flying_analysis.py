import matplotlib.pyplot as plt
import pycodamath as coda
import numpy as np
import pandas as pd
import scipy.stats as ss
from load_data import pokemon_data, colors
from custom_ternary import ternary

def closure_np(input, k):
    input_sum = np.sum(input)
    output = input * k/input_sum
    return output


pokemon_data_flying = pokemon_data[pokemon_data["Type 2"] == "Flying"]

covariates = pokemon_data_flying.iloc[:, 0:3]
closed_abilities = pokemon_data_flying.iloc[:, 3:].coda.closure(100)


sample_center = ss.mstats.gmean(closed_abilities)
sample_center = 100/np.sum(sample_center) * sample_center
print(sample_center)

var_matrix = closed_abilities.coda.varmatrix()

print(var_matrix)

total_variance = closed_abilities.coda.totvar()

print(total_variance)



clr = pow(closed_abilities/sample_center, 1./np.sqrt(total_variance)).coda.clr()
s, e, l = np.linalg.svd(clr)
# scale loadings with eigenvalues
l = np.inner(e*np.identity(6), l.T[0:6, 0:6])
# plots
# #1. Calculate the proportion of variance explained by each feature
# sum_eigenvalues = np.sum(e)
# prop_var = [i/sum_eigenvalues*100 for i in e]
# #2. Calculate the cumulative variance
# cum_var = [np.sum(prop_var[:i+1]) for i in range(len(prop_var))]
# # Plot scree plot from PCA
# x_labels = ['PC{}'.format(i+1) for i in range(len(prop_var))]
# plt.plot(x_labels, prop_var, marker='o', markersize=6, color='skyblue', linewidth=2, label='Proportion of variance')
# plt.plot(x_labels, cum_var, marker='o', color='orange', linewidth=2, label="Cumulative variance")
# plt.legend()
# plt.title('Scree plot')
# plt.xlabel('Principal components')
# plt.ylabel('Proportion of variance')
# plt.show()

# SCREE
fig, ax = plt.subplots()
myscree = coda.pca.scree_plot(axis = ax, eig_val = e)
plt.show()

## BIPLOT

mypca_type_1 = coda.pca.Biplot(closed_abilities)
mypca_type_1.removelabels()

mypca_type_1.plotloadings(cluster=True)
print(mypca_type_1.clusterlegend)
mypca_type_1.removelabels()
#mypca_type_1.removescores()
mypca_type_1.plotscores(group=covariates.iloc[:, 1], palette=colors, labels=covariates.iloc[:, 0])
#mypca_type_1.plotcentroids(group=covariates.iloc[:, 1], palette=colors)
#mypca_type_1.plotscorelabels(labels=covariates.iloc[:, 0])
#mypca_type_1.displaylegend(loc=1)
mypca_type_1.plotellipses(group=covariates.iloc[:, 1], palette=colors)
mypca_type_1.plotloadings(labels=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'], cluster=False)
mypca_type_1.adjustloadinglabels()
mypca_type_1.displaylegend(loc=1)

plt.show()



mypca_type_2 = coda.pca.Biplot(closed_abilities)
mypca_type_2.removelabels()

mypca_type_2.plotloadings(cluster=True)
print(mypca_type_2.clusterlegend)
mypca_type_2.removelabels()
#mypca_type_2.removescores()
mypca_type_2.plotscores(group=covariates.iloc[:, 2], palette=colors, labels=covariates.iloc[:, 0])
#mypca_type_2.plotcentroids(group=covariates.iloc[:, 2], palette=colors)
#mypca_type_2.plotscorelabels(labels=covariates.iloc[:, 0])
#mypca_type_2.displaylegend(loc=1)
mypca_type_2.plotellipses(group=covariates.iloc[:, 2], palette=colors)
mypca_type_2.plotloadings(labels=['HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'], cluster=False)
mypca_type_2.adjustloadinglabels()
mypca_type_2.displaylegend(loc=1)

plt.show()