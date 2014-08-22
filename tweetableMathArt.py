# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 09:48:11 2014
Project	:Python-Project
Version	:0.0.1
@author	:macrobull

"""

from math import *
import numpy as np
import cv2

DIM = 1024
DM1 = DIM - 1
_sq = lambda x:x*x
_cb = lambda x:abs(x*x*x)
_cr = lambda x:np.uint8(x**(1./3))

class Artist():
	WID = HEI = DIM
	title = "Default"

	def __init__(self):
		self.img = np.zeros((self.HEI, self.WID, 3), dtype = np.uint8)

	def RD(self, i, j):
		return (_sq(cos(atan2(j-512,i-512)/2))*255)

	def GR(self, i, j):
		return (_sq(cos(atan2(j-512,i-512)/2-2*acos(-1)/3))*255)

	def BL(self, i, j):
		return (_sq(cos(atan2(j-512,i-512)/2+2*acos(-1)/3))*255)

	def draw(self):
		for i in xrange(self.HEI):
			for j in xrange(self.WID):
				self.img[i,j,2] = int(self.RD(i,j)) & 255
				self.img[i,j,1] = int(self.GR(i,j)) & 255
				self.img[i,j,0] = int(self.BL(i,j)) & 255

		cv2.imshow(self.title, self.img)

if __name__ == "__main__":

	try:
		from tweetableMathArtist import *

	except BaseException:
		a = Artist()
		a.draw()

#	from tweetableMathArtist import *

#	a = HueSpin()
#	a.draw()
#
#	a = Martin_Buuttner()
#	a.draw()
#
#	a = Manuel_Kasten()
#	a.draw()

	a = ReflectedWaves()
	a.draw()

	import cv2
	while 27 != cv2.waitKey(0): pass
	cv2.destroyAllWindows()

