#!/usr/bin/python2.7
#Output is saved as MDS.png in your files section
import csv
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from sklearn import manifold
from matplotlib.font_manager import FontProperties


new_reader1 = pd.read_excel("aspiration_dissimilarity_matrix.xlsx")
result1 = new_reader1.values
result = result1[:,1:]
size = result.shape

for j in range(size[1]):
    for i in range(size[0]):
        result[i,j]=result[j,i]

new_reader = pd.DataFrame(result)

size_new= new_reader.shape

for j in range(size_new[1]):
    print j
    for i in range(size_new[0]):
        new_reader1.iloc[i,j+1]=new_reader.iloc[j,i]


adist = np.array(new_reader)
amax = np.amax(adist)
adist /= amax
print new_reader1
cities1 = [''.join(r).encode('utf-8') for r in list(new_reader1.iloc[0:,:1].values.tolist())]

mds = manifold.MDS(n_components=2, dissimilarity="precomputed", random_state=6)
results = mds.fit(adist)

coords = results.embedding_
plt.subplots_adjust(bottom = 0.1)
plt.scatter(
    coords[:, 0], coords[:, 1], marker = 'o'
    )
font0 = FontProperties()
font = font0.copy()

## Change the size of the font
## Sizes: ['xx-small', 'x-small', 'small', 'medium', 'large','x-large', 'xx-large']
font.set_size('xx-large')


for label, x, y in zip(cities1, coords[:, 0], coords[:, 1]):
    plt.annotate(
        label,
        xy = (x, y), xytext = (-20, 20),
         fontproperties=font,
        textcoords = 'offset points', ha = 'right', va = 'bottom',
        bbox = dict(boxstyle = 'round,pad=0.5', fc = 'yellow', alpha = 0.5),
        arrowprops = dict(arrowstyle = '->', connectionstyle = 'arc3,rad=0'))


plt.savefig('mds_new.png')
