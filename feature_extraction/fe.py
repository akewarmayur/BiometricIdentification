# Import functions and libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy
import cv2 as cv
from numpy import pi
from numpy import sin
from numpy import zeros
from numpy import r_
from scipy import signal
from scipy import misc
def extract_features_8x8(iris, fingerprint):
	iris_dct = block_8x8(iris)
	fingerprint_dct = block_8x8(fingerprint)
	# create vectors for each iris and fingerprint
	irisfv = (iris_dct.reshape(iris_dct.shape[0]*iris_dct.shape[1]))
	fingerprintfv = (fingerprint_dct.reshape(fingerprint_dct.shape[0]*fingerprint_dct.shape[1]))
	# concat the feature vectors
	fp_iris_fv =  np.concatenate((irisfv, fingerprintfv), axis=None)
	# Add the images
	#fp_iris_fv = cv.add(irisfv, fingerprintfv)
	# Convert back to image
	#combined_image = fp_iris_fv.reshape(450,450)
	return fp_iris_fv

#8x8
def block_8x8(im):
	# DCT transformation on finger print image using 8x8 block
	imsize = im.shape
	features = np.zeros(imsize)

	# Do 8x8 DCT on image (in-place)
	for i in r_[:imsize[0]:8]:
    		for j in r_[:imsize[1]:8]:
        		features[i:(i+8),j:(j+8)] = dct2( im[i:(i+8),j:(j+8)] )

	return features


# DCT and IDCT functions for transforming an image
def dct2(a):
    return scipy.fftpack.dct( scipy.fftpack.dct( a, axis=0, norm='ortho' ), axis=1, norm='ortho' )

def idct2(a):
    return scipy.fftpack.idct( scipy.fftpack.idct( a, axis=0 , norm='ortho'))


#4x4
def block_4x4(im):
	# DCT transformation on finger print image using 8x8 block
	imsize = im.shape
	features = np.zeros(imsize)

	# Do 8x8 DCT on image (in-place)
	for i in r_[:imsize[0]:4]:
    		for j in r_[:imsize[1]:4]:
        		features[i:(i+4),j:(j+4)] = dct2( im[i:(i+4),j:(j+4)] )

	return features

#16x16
def block_16x16(im):
	# DCT transformation on finger print image using 8x8 block
	imsize = im.shape
	features = np.zeros(imsize)

	# Do 8x8 DCT on image (in-place)
	for i in r_[:imsize[0]:16]:
    		for j in r_[:imsize[1]:16]:
        		features[i:(i+16),j:(j+16)] = dct2( im[i:(i+16),j:(j+16)] )

	return features

def extract_features_4x4(iris, fingerprint):
	iris_dct = block_4x4(iris)
	fingerprint_dct = block_4x4(fingerprint)
	# create vectors for each iris and fingerprint
	irisfv = (iris_dct.reshape(iris_dct.shape[0]*iris_dct.shape[1]))
	fingerprintfv = (fingerprint_dct.reshape(fingerprint_dct.shape[0]*fingerprint_dct.shape[1]))
	# concat the feature vectors
	fp_iris_fv =  np.concatenate((irisfv, fingerprintfv), axis=None)
	# Add the images
	#fp_iris_fv = cv.add(irisfv, fingerprintfv)
	# Convert back to image
	#combined_image = fp_iris_fv.reshape(450,450)
	return fp_iris_fv


def extract_features_16x16(iris, fingerprint):
	iris_dct = block_16x16(iris)
	fingerprint_dct = block_16x16(fingerprint)
	# create vectors for each iris and fingerprint
	irisfv = (iris_dct.reshape(iris_dct.shape[0]*iris_dct.shape[1]))
	fingerprintfv = (fingerprint_dct.reshape(fingerprint_dct.shape[0]*fingerprint_dct.shape[1]))
	# concat the feature vectors
	fp_iris_fv =  np.concatenate((irisfv, fingerprintfv), axis=None)
	# Add the images
	#fp_iris_fv = cv.add(irisfv, fingerprintfv)
	# Convert back to image
	#combined_image = fp_iris_fv.reshape(450,450)
	return fp_iris_fv

def extract_features_fp(fingerprint):
	fingerprint_dct = block_8x8(fingerprint)
	# create vectors for each iris and fingerprint
	#irisfv = (iris_dct.reshape(iris_dct.shape[0]*iris_dct.shape[1]))
	fingerprintfv = (fingerprint_dct.reshape(fingerprint_dct.shape[0]*fingerprint_dct.shape[1]))
	# concat the feature vectors
	fp_fv =  fingerprintfv
	# Add the images
	#fp_iris_fv = cv.add(irisfv, fingerprintfv)
	# Convert back to image
	#combined_image = fp_iris_fv.reshape(450,450)
	return fp_fv

def extract_features_iris(iris):
	iris_dct = block_8x8(iris)
	# create vectors for each iris and fingerprint
	#irisfv = (iris_dct.reshape(iris_dct.shape[0]*iris_dct.shape[1]))
	irisfv = (iris_dct.reshape(iris_dct.shape[0]*iris_dct.shape[1]))
	# concat the feature vectors
	iris_fv =  irisfv
	# Add the images
	#fp_iris_fv = cv.add(irisfv, fingerprintfv)
	# Convert back to image
	#combined_image = fp_iris_fv.reshape(450,450)
	return iris_fv
