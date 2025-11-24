#
import os.path as osp
import numpy as np

import pandas as pd
from plotnine import *
import matplotlib.pyplot as plt

def _plot_feature_importances(ID, importance, path=None, n_labels='all',
                              sort=False, suffix=None):
    n_features_ = len(importance)
    nb_bands_pos = np.arange(n_features_)
    bands_id = [str(n+1) for n in range(n_features_)]
    n_graph = 1
    x = 0

    if sort == True:
        tuples = [(str(k+1), importance[k]) for k in range(n_features_)]
        tuples = sorted(tuples, key=lambda x: x[1])
        tuples.reverse()
        bands_id, importance = zip(*tuples)
    
    if n_labels == 'all':
        nb_to_plot = n_features_
    else:
        nb_to_plot = n_labels
    for i in range(n_features_):
        if (i+1) % nb_to_plot == 0 :
            nb_bands_pos = np.arange(nb_to_plot)

            if suffix == None:
                title = 'Feature Importances #{}'.format(n_graph)
            else:
                title = 'Feature Importances #{0} {1}'.format(n_graph, suffix)

            df = pd.DataFrame({'x':nb_bands_pos, 'y':importance[x:i+1]})
            p = (ggplot(df) +
                 geom_col(aes('df.index', 'y')) +
                 xlab('Band #') +
                 ylab('Feature Importances Score') +
                 ggtitle(title) +
                 scale_x_continuous(breaks=nb_bands_pos, labels=bands_id[x:i+1]))
    
            if path != None:
                if suffix == None:
                    fout = osp.join(path, '{0}_feat_imp_{1}.png'.format(ID, n_graph))
                else:
                    fout = osp.join(path, '{0}_feat_imp_{1}_{2}.png'.format(ID, suffix, n_graph))
                try:
                    p.save(fout)
                except IOError:
                    raise IOError('in pysptools.sklearn.util._plot_feature_importances, no such file or directory: {0}'.format(path))
            else:
                p.draw()
            n_graph += 1
            x = i+1

    if x < n_features_:
        end = n_features_
        nb_bands_pos = np.arange(end-x)
#
        if suffix == None:
            title = 'Feature Importances #{}'.format(n_graph)
        else:
            title = 'Feature Importances #{0} {1}'.format(n_graph, suffix)

        df = pd.DataFrame({'x':nb_bands_pos, 'y':importance[x:end]})
        p = (ggplot(df) +
             geom_col(aes('df.index', 'y')) +
             xlab('Band #') +
             ylab('Feature Importances Score') +
             ggtitle(title) +
             scale_x_continuous(breaks=nb_bands_pos, labels=bands_id[x:end]))

        if path != None:
            if suffix == None:
                fout = osp.join(path, '{0}_feat_imp_{1}.png'.format(ID, n_graph))
            else:
                fout = osp.join(path, '{0}_feat_imp_{1}_{2}.png'.format(ID, suffix, n_graph))
            try:
                p.save(fout)
            except IOError:
                raise IOError('in pysptools.sklearn.util._plot_feature_importances, no such file or directory: {0}'.format(path))
        else:
            p.draw()

if __name__ == '__main__':
    imp = [23,1,4,20,10,3,4,5,12,13,11,9,8,7,6]
    result = '/home/cri/results'
    _plot_feature_importances('test', imp, path=result, n_labels=4, sort=False, suffix=None)
