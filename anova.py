import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pycodamath as coda
import scipy.stats as ss

from sklearn.linear_model import LinearRegression
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from load_data import pokemon_data, colors


pokemon_data = pokemon_data[pokemon_data["Type 1"].isin(["Fighting", "Psychic"])]
# pokemon_data = pokemon_data[pokemon_data["Type 2"].isin(["Flying", "Poison"])]


covariates = pokemon_data.iloc[:, 0:3]
closed_abilities = pokemon_data.iloc[:, 3:].coda.closure(100)

# Sample mean of full data set
closed_abilities.coda.gmean()

sample_center = ss.mstats.gmean(closed_abilities)


# Sorted CLRbeta1
#clrbeta1 = [-0.61, -0.48, -0.46, -0.45, -0.05, -0.04, 0.47, 0.48, 1.14]

# Build informed basis


# psy fight
balances = [[0, -1, 1, 0, 0, 0],
    [0, 0, 0, -1, 1, 0],
    [0, -1, -1, 1, 1, 0],
    [-1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, -1]]

psi = coda.extra.norm(balances)
ilr = closed_abilities.coda.ilr(psi)

# Rename columns for ols to work
for i in ilr.columns:
    ilr = ilr.rename(columns={i: 'ilr'+str(i)})

# add covariates
# IF ANALYZING FIGHTING / PSYCHIC --> Type 1
ilr['covariates'] = covariates['Type 1'].str[:5]

# IF ANALYZING POISON / FLYING --> Type 2
# ilr['covariates'] = covariates['Type 2'].str[:5]

print(ilr)
# Do ANOVA per part
for part in ilr.columns[:-1]:
    model = ols(part+' ~ covariates', data=ilr).fit()
    print(model.params)
    print(part)
    print('beta', model.params.iloc[1].round(2))
    print('t value', np.sqrt(model.fvalue).round(2))
    print('p value', model.pvalues.iloc[1].round(4))
    print()


beta = [ols(part + '~ covariates', data=ilr).fit().params.iloc[1] for part in ilr.columns[:-1]]
beta = pd.DataFrame(beta, columns=['beta'], index=ilr.columns[:-1]).T
clrbeta = pd.DataFrame(np.dot(beta, psi), index=['clrbeta'], columns=closed_abilities.columns)
print(clrbeta.iloc[0].sort_values())
