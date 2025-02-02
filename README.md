Course project for compositional data analysis

Descriptive and exploratory analysis of generation 1 Pokemon, treating their combat stats as compositions

load_data --> loads data into dataframe
descriptive_analysis --> bar plots of counts stratified by primary and secondary types
sample_mean_variance --> clr via sample center perturbation and total variance scaling for PCA biplots of entire data
amalgamations --> ternary plots of all stat type combinations using entire data
subcompositional --> ternary plots of re-perturbed and re-scaled subcompositions 
mono_analysis / flying_analysis --> additional subcomposition plots
anova --> one-way ANOVA of fighting/psychic and poison/flying subcompositions using basis for stat types defined from PCA in 'sample_mean_variance'


Compositional analysis performed using pyCoDaMath package: https://bitbucket.org/genomicepidemiology/pycodamath/src/master/
custom_svd and custom_ternary scrips are modified for this project from the pyCoDaMath package
