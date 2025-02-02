import ternary as td
import numpy as np
import pandas as pd
from pycodamath import extra


def ternary(data, descr=None, center=False, conf=False, colors_dict=None, line_data=None): #, line_data=None, scaling_factor=None, gmean=None):
    ''' Plot ternary diagram '''
    if np.shape(data)[1] > 3:
        raise AttributeError("Error: Too many parts in composition (max. 3).")
    for column in data.T:
        if np.abs(data.T[column].sum()-100.) > 1e-6:
            raise AttributeError("Error: Composition is not closed to 100.")

    _, tax = td.figure(scale=100)
    tax.boundary(linewidth=1.5)
    tax.gridlines(color="blue", multiple=10, linewidth=0.5, alpha=0.5)
    tax.left_axis_label(f"% {data.columns[0]:s}", fontsize=16, offset=0.14)
    tax.right_axis_label(f"% {data.columns[1]:s}", fontsize=16, offset=0.14)
    tax.bottom_axis_label(f"% {data.columns[2]:s}", fontsize=16, offset=0.12)
    tax.ticks(axis='lbr', linewidth=1, multiple=10, offset=0.03)
    tax.clear_matplotlib_ticks()
    tax.get_axes().axis('off')

    if center:
        sdata = (data/data.coda.gmean()).coda.closure(100)
    else:
        sdata = data

    if descr is not None:
        if colors_dict is not None:
            for group in set(descr):
                idx = descr.loc[descr == group].index
                tax.scatter(sdata.loc[idx, [sdata.columns[2], sdata.columns[1],
                                            sdata.columns[0]]].values, alpha=0.7, 
                                            color=colors_dict[group],
                                            label=group)
                
        else:
            for group in set(descr):
                idx = descr.loc[descr == group].index
                tax.scatter(sdata.loc[idx, [sdata.columns[2], sdata.columns[1],
                                            sdata.columns[0]]].values, alpha=0.7)
            
    else:
        tax.scatter(sdata.loc[:, [sdata.columns[2], sdata.columns[1],
                                  sdata.columns[0]]].values, alpha=0.7,
                    color='steelblue')

    if conf:
        ilr = sdata.coda.ilr().loc[:, [0, 1]]
        par = extra.get_covariance_ellipse(ilr)

        points = [[par['center'][0] +
                   par['shape'][0]*np.cos(par['angle'])*np.cos(a) -
                   par['shape'][1]*np.sin(par['angle'])*np.sin(a),
                   par['center'][1] +
                   par['shape'][0]*np.cos(par['angle'])*np.sin(a) +
                   par['shape'][1]*np.sin(par['angle'])*np.cos(a)]
                  for a in np.linspace(0, 2*np.pi, 100)]

        psi = extra.sbp_basis(sdata)

        ellipse = pd.DataFrame(np.exp(np.matmul(points, psi))).coda.closure(100)
        ellipse = ellipse.loc[:, [ellipse.columns[1], ellipse.columns[0],
                                  ellipse.columns[2]]]
        tax.plot(ellipse.values, color='black', lw=0.5, ls='-')
        tax.legend()

    if line_data is not None:
        tax.plot(line_data,  color='black', lw=0.5, ls='-')


    return tax