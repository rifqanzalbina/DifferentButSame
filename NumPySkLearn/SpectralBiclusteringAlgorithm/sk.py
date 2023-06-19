# Import Library
import numpy as np
from matplotlib import pyplot as plt
from sklearn.datasets import make_checkerboard
from sklearn.cluster import SpectralBiclustering
from sklearn.metrics import consensus_score

# === Codes === 
n_cluster = (4,3)
data, rows, columns = make_checkerboard(
    shape=(300,300), n_clusters=n_cluster, noise=10, shuffle=False, random_state=0
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original Dataset")

rng = np.random.RandomState(0)
row_idx = rng.permutation(data.shape[0])
col_idx = rng.permutation(data.shape[0])
data = data[row_idx][:,col_idx]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled Dataset")

model = SpectralBiclustering(n_clusters=n_cluster, method="log",random_state=0)
model.fit(data)
score = consensus_score(model.biclusters_, (rows[:,row_idx],columns[:,col_idx]))

print("Consensus score : {:.1f}".format(score))

fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]

plt.matshow(fit_data, cmap=plt.cm.Blues)
plt.title("After Biclustering : rearranged to show biclusters")

plt.matshow(
    np.outer(np.sort(model.row_labels_) + 1, np.sort(model.column_labels_) + 1),
    cmap=plt.cm.Blues,
)

plt.title("CheckerBoard structure of rearranged data")

plt.show()
# === Endcode ===