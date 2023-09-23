"""
Name: Eric Zheng
Date:12/2/2021
"""

import pandas as pd
import numpy as np
from sklearn.cluster import MiniBatchKMeans
import warnings; warnings.simplefilter('ignore')
from matplotlib import image as img
from matplotlib import pyplot as plt



def coloring(img, n_clusters = 4, random_state=5):
	data = img / 255.0
	
	data = data.reshape(427 * 640, 3)

	kmeans = MiniBatchKMeans(n_clusters,random_state=random_state)
	kmeans = kmeans.fit(data)
	y_kmeans = kmeans.predict(data)
	new_colors = kmeans.cluster_centers_[y_kmeans]
	

	recolored = new_colors.reshape(img.shape)

	return recolored
	
imagename = input()
picture =img.imread(imagename)
picture_4col = p50.coloring(picture)
fig, ax = plt.subplots(1, 2, figsize=(16, 6),subplot_kw=dict(xticks=[], yticks=[]))
fig.subplots_adjust(wspace=0.05)
ax[0].imshow(picture)
ax[0].set_title('Original Image', size=16)
ax[1].imshow(picture_4col)
ax[1].set_title('4-color Image', size=16);
plt.show()










