# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# %matplotlib qt

import glob
import imageio
import numpy
import matplotlib as mpl
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
# plt.interactive(True)
mpl.rcParams['figure.dpi'] = 300

# Load images
images_paths = glob.glob('chest_array/*')
images_paths.sort()

images = []
for image_path in images_paths:
    images.append(imageio.imread(image_path))


# Read meta
slice_spacing = images[0].meta['SliceSpacing']*5
pixel_spacing_x = images[0].meta['PixelSpacing'][0]
pixel_spacing_y = images[0].meta['PixelSpacing'][1]
image_position_patient = images[0].meta['ImagePositionPatient']

# Create mesh
X = numpy.arange(0, 256) * pixel_spacing_x + image_position_patient[0]
Y = numpy.arange(0, 256) * pixel_spacing_y + image_position_patient[1]
X, Y = numpy.meshgrid(X, Y);

# Plot
Z = X + image_position_patient[2]
fig = plt.figure()
ax = fig.gca(projection='3d')

for i, image in enumerate(images):
    ax.plot_surface(X, Y, Z + i*slice_spacing, rstride=1, cstride=1, facecolors = cm.gray(image[::-1]))

plt.savefig('stacked_ct_planes.png')