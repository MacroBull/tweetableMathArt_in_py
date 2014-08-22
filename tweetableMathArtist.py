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

class TableCloth_color(Artist):
	title = "githubphagocyte:TableCloth-Color"

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

class TableCloth_flat(Artist):
	title = "githubphagocyte:TableCloth-Flat"

	def RD(self, j, i):
		s=3./(j+99);
		return (int((i+DIM)*s+j*s)%2+int((DIM*2-i)*s+j*s)%2)*127;

	def GR(self, j, i):
		s=3./(j+99);
		return (int((i+DIM)*s+j*s)%2+int((DIM*2-i)*s+j*s)%2)*127;

	def BL(self, j, i):
		s=3./(j+99);
		return (int((i+DIM)*s+j*s)%2+int((DIM*2-i)*s+j*s)%2)*127;

MAXINT32 = 4294967295
DAP = 1000000000
COLD = 256 / 2 - 1
class TableCloth_flat_fixed(Artist):
	title = "githubphagocyte:TableCloth-Flat in fixed int"

	def RD(self, j, i):
		s=MAXINT32/(j+99) # altitude and elevation
		return ( (((i+DIM)*s / DAP) & 1)
			+ ( ((DIM*2-i)*s / DAP) & 1) ) * COLD;

	def GR(self, j, i):
		return self.RD(j,i)

	def BL(self, j, i):
		return self.RD(j,i)

v = s = y = 0
#(743, 897 -- 0, 452)
class TableCloth_color_fixed(Artist):
	title = "githubphagocyte:TableCloth-Color in fixed int"

	def RD(self, j, i):
		global v, s, y
#		v = int(50. * (DIM/2 - (abs(DIM / 2 - i)-1)) ** -0.05)
		s=MAXINT32/(j+99) # altitude and elevation

#		v = (i+j)

		y=DIM/2 - abs(DIM/2 - i) - j * 445 / 743
		return ( (((i+DIM + y)*s / DAP) & 1)
			+ ( ((DIM*2-i + y)*s / DAP) & 1) ) * COLD;

	def GR(self, j, i):
		return ( ((5* (i+DIM + y)*s / DAP) & 1)
			+ ( (5* (DIM*2-i + y)*s / DAP) & 1) ) * COLD;

	def BL(self, j, i):
		return ( ((29*(i+DIM + y)*s / DAP) & 1)
			+ ( (29*(DIM*2-i + y)*s / DAP) & 1) ) * COLD;


w = 30  # target radius

class ReflectedWaves(Artist):
	title = "githubphagocyte:ReflectedWaves"

	def RD(self, j, i):
		return 0

	def GR(self, j, i):
		return 0

	def BL(self, j, i):
		x = i; y = j
#		for a in loop:
#			for b in loop:
		l = i - 500
		k = j  - 500
		r = sqrt(l*l+k*k)  # distance
		d = 16*cos((r-w)/7) * exp(-_sq(r-w)/12)
		if r>0:
			p = d*l/r
			q = d*k/r
			x -= p
			y -=q


		return ((int(x/64)+int(y/64))&1) *255;

class WaveLines(Artist):
	title = "WaveLines"

	def RD(self, j, i):
		return 0

	def GR(self, j, i):
		return 0

	def BL(self, j, i):
		d = 16*cos((i+j-w)/7) * exp(-_sq(i+j-w)/12)
		i -= d
		j -= d


		return ((int(i/64) + int(j/64))&1) *255;
