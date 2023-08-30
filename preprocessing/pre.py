# Import functions and libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy
import cv2 as cv
from scipy import misc # pip install Pillow
def pre(image):
	img = misc.imresize(image, (280, 320))
	#img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	return img
