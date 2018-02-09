import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
from numpy.linalg import norm
from math import *


def drawplot():
	mu = 0
	sigma = 1
	x = np.arange(0, 6, 0.1)

	y = stats.norm.pdf(x, 0, 1)
	z = stats.t.pdf(x, 1)
	plt.plot(x, y, label="Norm distribution")
	plt.plot(x, z, label="t distribution")
	plt.title('Normal Distribution and t Distribution')
	#plt.title('Normal')
	plt.xlabel('x')
	plt.ylabel('Probablity density')
	plt.legend() 
<<<<<<< HEAD
	plt.plot([0, 6], [0.025, 0.025], 'r--')
	plt.plot([0, 6], [0.2, 0.2], 'r--')
=======
	plt.plot([0, 6], [0.025, 0.025], 'r--', linewidth = 0.7)
	plt.plot([0, 6], [0.2, 0.2], 'r--', linewidth = 0.7)
>>>>>>> 6b06b07cc24c0a966abe5651bea050cb254bcfc9
	tx1 = 0.5
	ty1 = 0.2
	plt.text(tx1, ty1, "$q_{ij}$",fontdict=None, withdash=False,fontsize=13)
	tx2 = 1.4
	ty2 = 0.2
	plt.text(tx2, ty2, "$p_{ij}$",fontdict=None, withdash=False,fontsize=13)
	tx3 = 2.0
	ty3 = 0.025
	plt.text(tx3, ty3, "$p_{ij}$",fontdict=None, withdash=False,fontsize=13)
	tx4 = 3.5
	ty4 = 0.025
	plt.text(tx4, ty4, "$q_{ij}$",fontdict=None, withdash=False,fontsize=13)
	plt.show()


if __name__ == "__main__":
	drawplot()