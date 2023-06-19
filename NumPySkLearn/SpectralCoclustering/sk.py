# Import libraries
from matplotlib import pyplot as plt
import numpy as np


# === Codes ===
from sklearn.datasets import make_biclusters
from sklearn.cluster import SpectralCoclustering
from sklearn.metrics import consensus_score

data, rows, columns = make_biclusters(
    shape=(800,600), n_clusters=5, noise=5, shuffle=False, random_state=0
)

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Original Dataset")

# Shuffle Clasters 
rng = np.random.RandomState(0)
row_ldx = rng.permutation(data.shape[0])
col_ldx = rng.permutation(data.shape[1])
data = data[row_ldx][:, col_ldx]

plt.matshow(data, cmap=plt.cm.Blues)
plt.title("Shuffled Data")

model = SpectralCoclustering(n_clusters=5,random_state=0)
model.fit(data)
score = consensus_score(model.biclusters_,(rows[:, row_ldx], columns[:, col_ldx]))

print("Consensus score : {:.3f}".format(score))

fit_data = data[np.argsort(model.row_labels_)]
fit_data = fit_data[:, np.argsort(model.column_labels_)]

plt.matshow(fit_data, cmap=plt.cm.Blues)
plt.title("After biclustering; rearranged to show biclusters")

plt.show()
# === EndCodes ===
