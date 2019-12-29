import numpy as np
from . import DCT


def denoise(image, sigma):
	"""Denoise given image

	Keyword arguments:
	image -- Float NumPy array. Represents Gray scale image.
	sigma -- Denoise strength parameter.
	"""
	if len(image.shape) > 2:
		raise ValueError('Only gray scale images supported')

	width = image.shape[1]
	height = image.shape[0]
	channels = 1

	treshold = 3 * sigma

	patches = np.zeros((height - DCT.PATCHSIZE, width - DCT.PATCHSIZE, DCT.PATCHSIZE, DCT.PATCHSIZE))

	# 2D DCT forward
	for i in range(height - DCT.PATCHSIZE):
		for j in range(width - DCT.PATCHSIZE):
			patches[i, j,:,:] = DCT.DCT2D(image[i:i + DCT.PATCHSIZE, j:j + DCT.PATCHSIZE], True)

	# Thresholding
	np.where(patches < treshold, 0, patches)

	# 2D DCT inverse
	#inverse = np.vectorize(lambda x: DCT2D(x, False))
	for i in range(height - DCT.PATCHSIZE):
		for j in range(width - DCT.PATCHSIZE):
			patches[i, j, :, :] = DCT.DCT2D(patches[i, j], False)

	# Assemble new image
	result = np.zeros((height, width))
	weights = np.zeros((height, width))
	for i in range(height - DCT.PATCHSIZE):
		for j in range(width - DCT.PATCHSIZE):
			for ip in range(DCT.PATCHSIZE):
				for jp in range(DCT.PATCHSIZE):
					result[i + ip, j + jp] += patches[i][j][ip][jp]
					weights[i + ip, j + jp] += 1

	result /= weights

	return result


def noise(image):
	"""Add noise to given image

	Keyword arguments:
	image -- Float NumPy array. Represents Gray scale image.
	"""
	mean = 0; var = 0.001; sigma = var**0.5
	
	noise = np.random.normal(0, sigma, image.shape)
	
	maxVal = np.max(image)
	minVal = np.min(image)
	norm = np.float64((image - minVal) / (maxVal - minVal))

	noisy = norm + noise
	minNoisy = np.min(noisy)
	maxNoisy = np.max(noisy)
	noisy = np.round((noisy - minNoisy) * 255 / (maxNoisy - minNoisy))

	return np.float64((noisy - np.min(noisy)) / (np.max(noisy) - np.min(noisy)))
