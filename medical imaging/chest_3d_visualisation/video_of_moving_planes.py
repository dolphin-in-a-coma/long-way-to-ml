# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 18:58:08 2021

@author: eugen
"""

# %matplotlib qt

import glob
import imageio
import numpy
from matplotlib import pyplot as plt
from matplotlib import cm
import matplotlib.animation as animation
# plt.interactive(True);

# Load images
images_paths = glob.glob('chest_array/*')
images_paths.sort()

images = []
for image_path in images_paths:
    images.append(imageio.imread(image_path))

# To make images different
for i in range(1,len(images)):
    images[i] = images[i-1] ** 1.2

frames = [] # for storing the generated images
fig = plt.figure()
for image in images:
    frames.append([plt.imshow(image, cmap=cm.Greys_r,animated=True)])
    plt.axis('off')

ani = animation.ArtistAnimation(fig, frames, interval=200, blit=True,
                                repeat_delay=0)

ani.save('moving_through_planes.gif')
plt.show()