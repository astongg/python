# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np

# <codecell>

muvec = np.array([-.51864, 4.70574, -.69862])/100
Onevec = np.ones([len(muvec)])
PS1_V = np.matrix([[0.001005,	0.001328,	-0.000579,	-0.000675,	0.000121,	0.000128,	-0.000445,	-0.000437],
               [0.001328,	0.007277,	-0.001307,	-0.000610,	-0.002237,	-0.000989,	0.001442,	-0.001535],
               [-0.000579,	-0.001307,	0.059852,	0.027588,	0.063497,	0.023036,	0.032967,	0.048039],
               [-0.000675,	-0.000610,	0.027588,	0.029609,	0.026572,	0.021465,	0.020697,	0.029854],
               [0.000121,	-0.002237,	0.063497,	0.026572,	0.102488,	0.042744,	0.039943,	0.065994],
               [0.000128,	-0.000989,	0.023036,	0.021465,	0.042744,	0.032056,	0.019881,	0.032235],
               [-0.000445,	0.001442,	0.032967,	0.020697,	0.039943,	0.019881,	0.028355,	0.035064],
               [-0.000437,	-0.001535,	0.048039,	0.029854,	0.065994,	0.032235,	0.035064,	0.079958]])

V = np.matrix([[.0056, -.002, .0037],
			   [-.002, .0022, -.0022],
			   [.0037, -.0022, .0074]])
rf = .01

# <codecell>

A = 2*V
A

# <codecell>

B = np.append(A, [muvec], axis=0)
B

# <codecell>

C = np.append(B, [Onevec], axis=0)
C

# <codecell>

D = np.insert(C, 3, np.append(muvec, [0,0])*-1, axis=1)
D

# <codecell>

E = np.insert(D, 4, np.append(Onevec, [0,0])*-1, axis=1)
E

# <codecell>

b = np.matrix([0,0,0,.05,1])
b

# <codecell>

print(E.I * b.T)

# <codecell>

