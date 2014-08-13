# -*- coding: utf-8 -*-
"""
Created on Wed Aug 13 10:11:29 2014
Project	:Python-Project
Version	:0.0.1
@author	:macrobull

"""

from math import *
from tweetableMathArt import DIM, DM1, _sq, _cb, _cr, Artist


class HueSpin(Artist):
	title = "HueSpin"
	def RD(self, i, j):
		return (_sq(cos(atan2(j-512,i-512)/2))*255)

	def GR(self, i, j):
		return (_sq(cos(atan2(j-512,i-512)/2-2*acos(-1)/3))*255)

	def BL(self, i, j):
		return (_sq(cos(atan2(j-512,i-512)/2+2*acos(-1)/3))*255)


from numpy import *
from numpy.random import randint as r

cr = zeros((DIM, DIM))
cg = zeros((DIM, DIM))
cb = zeros((DIM, DIM))

class Martin_Buuttner(Artist):
	title = "Martin Büttner"

	def RD(self, i, j):
		if 0 == cr[i][j]:
			if ((i<2)or(j<2)):
				cr[i][j] = 1
			elif (0 == r(999)):
				cr[i][j] = r(256)
			else:
				cr[i][j] = self.RD(i - r(2), j -r(2))
		return cr[i][j]

	def GR(self, i, j):
		if 0 == cg[i][j]:
			if ((i<2)or(j<2)):
				cg[i][j] = 1
			elif (0 == r(999)):
				cg[i][j] = r(256)
			else:
				cg[i][j] = self.GR(i - r(2), j -r(2))
		return cg[i][j]

	def BL(self, i, j):
		if 0 == cb[i][j]:
			if ((i<2)or(j<2)):
				cb[i][j] = 1
			elif (0 == r(999)):
				cb[i][j] = r(256)
			else:
				cb[i][j] = self.BL(i - r(2), j -r(2))
		return cb[i][j]

from numpy.random import rand
kr = kg = kb = 0

class Manuel_Kasten(Artist):
	title = "Manuel Kasten"

	def RD(self, i, j):
		global kr
		kr+=rand()
		l = int(kr) % 512
		return 511-l if l>255 else l

	def GR(self, i, j):
		global kg
		kg+=rand()
		l = int(kg) % 512
		return 511-l if l>255 else l

	def BL(self, i, j):
		global kb
		kb+=rand()
		l = int(kb) % 512
		return 511-l if l>255 else l

class githubphagocyte(Artist):
	title = "githubphagocyte"

	def RD(self, j, i):
		s=3./(j+99);
		y=(j+sin((i*i+_sq(j-700)*5)/100./DIM)*35)*s;
		return (int((i+DIM)*s+y)%2+int((DIM*2-i)*s+y)%2)*127;

	def GR(self, j, i):
		s=3./(j+99);
		y=(j+sin((i*i+_sq(j-700)*5)/100./DIM)*35)*s;
		return (int(5*((i+DIM)*s+y))%2+int(5*((DIM*2-i)*s+y))%2)*127;

	def BL(self, j, i):
		s=3./(j+99);
		y=(j+sin((i*i+_sq(j-700)*5)/100./DIM)*35)*s;
		return (int(29*((i+DIM)*s+y))%2+int(29*((DIM*2-i)*s+y))%2)*127;
