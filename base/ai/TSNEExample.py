#!/usr/bin/python
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE

digits = load_digits()

tsne = TSNE(random_state=42)
digits_tsne = tsne.fit_transform(digits.data)

tsnefig = plt.plot(20, 20)
tsnefig = plt.figure(figsize=(10, 10))
tsnefig = plt.xlim(digits_tsne[:, 0].min(), digits_tsne[:, 0].max() + 1)
tsnefig = plt.ylim(digits_tsne[:, 1].min(), digits_tsne[:, 1].max() + 1)

print(digits.data)
for i in range(len(digits.data)):
    plt.text(digits_tsne[i, 0], digits_tsne[i, 1], str(digits.target[i]))

tsnefig = plt.xlabel("t-sne feature 0")
tsnefig = plt.xlabel("t-sne feature 1")
tsnefig.figure.savefig("tsnefig", bbox_inches='tight')


