import pandas as pd
import numpy as np

from sklearn import manifold, datasets
from time import time


# options
random_state = 0
n_samples = 1000
n_components = 3
perplexity = 30

data_train_not_susp_file = 'data/train_not_susp.csv'
data_train_not_susp = pd.read_csv(data_train_not_susp_file)
data_train_not_susp = data_train_not_susp[:100]

# load the data and randomly sample
data_train_susp_file = 'data/train_susp.csv'
data_train_susp = pd.read_csv(data_train_susp_file)
data_train_susp = data_train_susp[:100]

data_prediction_file = 'data/predictions.csv'
data_prediction = pd.read_csv(data_prediction_file)
data_prediction = data_prediction[:100]

# define TSNE
tsne = manifold.TSNE(n_components=n_components, init='random', n_iter=1000, learning_rate=200.0,
                    random_state=random_state, perplexity=perplexity, verbose=1, method='exact')

Y_no_susp = tsne.fit_transform(data_train_not_susp.values)
Y_susp = tsne.fit_transform(data_train_susp.values)
Y_pred_susp = tsne.fit_transform(data_prediction.values)

# concatenate and save
Y = np.concatenate((np.array(Y_no_susp), np.array(Y_susp), np.array(Y_pred_susp)), axis=1)
print(Y.shape)
df = pd.DataFrame(Y)
df.to_csv("tsne_projections.csv", index=False)