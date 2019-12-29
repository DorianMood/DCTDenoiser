import numpy as np
from matplotlib import pyplot as plt
import cv2

import DCT

# Read image
fileName = 'tram256.png'
image = np.float64(cv2.imread(fileName, 0))

# Create noised and denoised images
imageN = DCT.noise(image)
imageD = DCT.denoise(image, 15)


# Show the results
fig, ax = plt.subplots(1, 3, figsize=[15, 5])

ax[0].imshow(image, cmap=plt.cm.gray)
ax[1].imshow(imageN, cmap=plt.cm.gray)
ax[2].imshow(imageD, cmap=plt.cm.gray)

plt.show()
