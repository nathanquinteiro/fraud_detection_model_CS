import pandas as pd
import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import NullFormatter
from sklearn import manifold, datasets
from time import time

# options
random_state = 1234
n_samples = 1000
n_components = 3
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
perplexity = 5

# load the data and randomly sample
data_file_path = 'data/final_train.csv'
data = pd.read_csv(data_file_path).sample(n=n_samples, random_state=random_state)

# spearate features from the labels
y = data['suspicious']
X = data.drop(['suspicious'], axis=1)

# convert to numpy arrays
y = y.values
X = X.values

# get the boolean masks
not_suspicious = y == 0
suspicious = y == 1


    
# fit the TSNE
t0 = time()
tsne = manifold.TSNE(n_components=n_components, init='random',
                    random_state=random_state, perplexity=perplexity, verbose=1, method='exact')
Y = tsne.fit_transform(X)
t1 = time()
    
print("perplexity=%d in %.2g sec" % (perplexity, t1 - t0))
ax.set_title("Perplexity=%d" % perplexity)
ax.scatter(Y[not_suspicious, 0], Y[not_suspicious, 1], Y[not_suspicious, 2], c="g", label='not suspicious', marker='o')
ax.scatter(Y[suspicious, 0], Y[suspicious, 1], Y[suspicious, 2], c="r", label='suspicious', marker='^')
ax.legend(loc='upper left')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()