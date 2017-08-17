import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as op

def plotData(X, Y, stringX, stringY):
	#np.extract(Y==1,X[0]) returns an array of values in X where the value is 1 in the same location in Y
	positiveExamples = plt.scatter(np.extract(Y==1,X[:,0]), np.extract(Y==1,X[:,1]), label = "y=1", marker='o', color='b', s=10)
	negativeExamples = plt.scatter(np.extract(Y==0,X[:,0]), np.extract(Y==0,X[:,1]), label = "y=0", marker='x', color='r', s=10)	
	plt.legend(handles=[positiveExamples, negativeExamples], loc='lower left')
	plt.xlabel('Exam 1 Score')
	plt.ylabel('Exam 2 Score')
	plt.show()
	

def sigmoid(z):
	return np.array([1/(1+np.exp(-z))]).transpose()


def costFunction(theta, x, y):
	m = x.shape[0]
	z = sigmoid(np.matmul(x,theta))
	J = -1/m*(np.sum(np.log(z)*y+np.log(1-z)*(1-y)))
	return J

def gradient(theta, x, y):
	m = x.shape[0]
	z = sigmoid(np.matmul(x,theta))
	positiveExamples = plt.scatter(np.extract(Y==1,X[:,1]), np.extract(Y==1,X[:,2]), label = "y=1", marker='o', color='b', s=10)
	negativeExamples = plt.scatter(np.extract(Y==0,X[:,1]), np.extract(Y==0,X[:,2]), label = "y=0", marker='x', color='r', s=10)	
	#Only need 2 points to define a line, so choose two endpoints
	plot_x = np.array([min(X[:, 2]),  max(X[:, 2])])
	# Calculate the decision boundary line
	plot_y = (-1./theta[2])*(theta[1]*plot_x + theta[0])
	# Plot, and adjust axes for better viewing
	plt.plot(plot_x, plot_y)

	plt.legend(handles=[positiveExamples, negativeExamples], loc='lower left')
	plt.xlabel(stringX)
	plt.ylabel(stringY)
	plt.show()

def mapFeatures(X):
	degrees = 6

	[m,n] = X.shape
	for i in range(1, degrees):
		for j in range(0,i):
			r = np.multiply(np.power(X[:,0],i-j),np.power(X[:,1],j))
			X = np.append(X,r[:,np.newaxis],axis=1)

	X = np.insert(X,0,1,axis=1)

	return X
	