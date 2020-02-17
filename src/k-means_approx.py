#K-Means approximated Implementaion:
#Raiti Mario O55000434
#Nardo Gabriele Salvatore O55000430

# Precise Version --> tolerance = 0.0000 ( default value ) 
# Approximated Version --> tolerance > 0.0000 , choose a lower value for max_iteration

#Using as input a CSV file containig all the point to process

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd


style.use('ggplot')

class K_Means:
	def __init__(self, k, tolerance, max_iterations):
		self.k = k
		self.tolerance = tolerance
		self.max_iterations = max_iterations
		

	def fit(self, data): 

		self.centroids = {} #initialize a dictionary to save centroids coordinates

		for i in range(self.k):
			self.centroids[i] = data[i] #initialize centroids matrix to the firsts elements in the data matrix

		#begin iterations
		for i in range(self.max_iterations): #execute algorithm if iterations < max_iterations
			self.classes = {} #initialize clusters dictionary
			for i in range(self.k):
				self.classes[i] = [] #initialize an array for every cluster(number of centroids -> k)

			#find the distance between the point and cluster; choose the nearest centroid
			for features in data:
				distances = [np.linalg.norm(features - self.centroids[centroid]) for centroid in self.centroids] #'distances' store the distances from each elements to the k centroids
				classification = distances.index(min(distances)) #'classification' store for each element the index of the cluster based on the min distance from each centroid
				self.classes[classification].append(features) #append each element to its cluster (classes[classification] where classification is the index that identify the cluster)

			previous = dict(self.centroids)

			#average the cluster datapoints to re-calculate the centroids
			for classification in self.classes:
				self.centroids[classification] = np.average(self.classes[classification], axis = 0)

			isOptimal = True

			for centroid in self.centroids:

				original_centroid = previous[centroid]
				curr = self.centroids[centroid]

				if np.sum((curr - original_centroid)/original_centroid * 100.0) > self.tolerance:
					isOptimal = False

			#break out of the main loop if the results are optimal, ie. the centroids don't change their positions much(more than our tolerance)
			if isOptimal:
				break

def main(path,k=3,tolerance=0.0000, max_iterations=500): #set arguments(k,tolerance and max_iterations) to default value if they're no passed
	
	
	df = pd.read_csv(path) #read the data source from the path argument
	df = df[['V1', 'V2']]  #V1 and V2 headers of the df dataframe

	X = df.values #returns a numpy array
	print(df)
	print(X)
	
	km = K_Means(k, tolerance, max_iterations) #instantiate km of K_Means class
	km.fit(X) # perform the algorithm

	# Plotting the results
	print("Start Plotting..")
	colors = 10*["r", "g", "c", "b", "k"] #array of colors for cluster assignment

	for centroid in km.centroids:
		color = colors[centroid] #assign colors to centroid for plotting
		plt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], c = color , s = 80, marker= "X") #plot centroids

	for classification in km.classes:
		color = colors[classification] #assign colors to clusters for plotting
		for features in km.classes[classification]:
			plt.scatter(features[0], features[1], color = color,s = 30, alpha= 0.4) #plot clusters
	plt.show()

if __name__ == "__main__":
	main(path='../dataset/k_means_clustering_test_1.csv') #set arguments for main function (path, k, tolerance, max_iterations)