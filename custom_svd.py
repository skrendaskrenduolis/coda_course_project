import numpy as np
import pandas as pd

def custom_svd(clr):
    ''' Internal SVD function '''
    scores, eig_val, loadings = np.linalg.svd(clr)
    scores = pd.DataFrame(
        scores.T[0:2, :], columns=clr.index, index=['pc1', 'pc2', 'pc3'])
    loadings = pd.DataFrame(np.inner(eig_val*np.identity(len(eig_val)),
                                     loadings.T[0:len(eig_val), 0:len(eig_val)])[0:2],
                            columns=clr.columns[0:len(eig_val)], index=['pc1', 'pc2', 'pc3'])
    return scores, eig_val, loadings