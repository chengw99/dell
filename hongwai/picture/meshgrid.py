
"""
Created on Wed Oct 11 17:35:02 2017

@author: DELL
"""

import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
points=np.arange(-5,5,0.01)
xs,ys = np.meshgrid(points,points)
z=np.sqrt(xs**3+ys)

ax = fig.add_subplot(221)
ax.imshow(z);
ax = fig.add_subplot(222)
ax.imshow(z,cmap=plt.cm.gray)
ax = fig.add_subplot(223)
ax.imshow(z,cmap=plt.cm.cool)
ax = fig.add_subplot(224)
ax.imshow(z,cmap=plt.cm.hot)