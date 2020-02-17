#K-Means approximated Implementaion:
#Raiti Mario O55000434
#Nardo Gabriele Salvatore O55000430

# Precise Version --> approx_error = 0.0000 ( default value ) 
# Approximated Version --> approx_error > 0.0000 , choose iterations < default iter

#A CSV file containig all the point to process is used as input

import pandas as pand
import numpy as nump
import matplotlib.pyplot as pyplt
from matplotlib import style

style.use('ggplot')

class K_Means_Alg: 	#class K-Means_Alg define attributes and methods to perform the algorithm
	def __init__(self, n, approx_error, iterations):
		self.approx_error = approx_error				#set the approx factor
		self.iterations = iterations    				#set the number of iterations
		self.n = n 										#set the number of clusters/centroids
		

	def exe(self, data):   #exe method perform the algorithm

		self.centroids = {} #initialize dictionary to save centroids coordinates

		for i in range(self.n):
			self.centroids[i] = data[i] #initialize centroids matrix to the firsts elements in the data matrix

		#iterations
		for i in range(self.iterations):
			self.clusters = {} #initialize clusters dictionary
			for i in range(self.n):
				self.clusters[i] = [] #initialize an array for every cluster(number of centroids -> n)

			#choose the nearest centroid based on the distance from the point
			for point in data:
				distances = [nump.linalg.norm(point - self.centroids[centroid]) for centroid in self.centroids] #'distances' store the distances from each elements to the n centroids
				pointclass = distances.index(min(distances)) #'pointclass' store for each element the index of the cluster based on the min distance from each centroid
				self.clusters[pointclass].append(point) #append each element to its cluster (clusters[pointclass] where pointclass is the index that identify the cluster)

			previous = dict(self.centroids) #store centroids to compare them later to new re-calculated centroids

			#average the cluster datapoints to re-calculate the centroids
			for pointclass in self.clusters:
				self.centroids[pointclass] = nump.average(self.clusters[pointclass], axis = 0) #centroids[] now contains the coordinates of the new recalculated centroids

			end = True #end is used to verify if the algorithm has converged

			for centroid in self.centroids:
				original_centroid = previous[centroid]
				curr = self.centroids[centroid]

				if nump.sum((curr - original_centroid)/original_centroid * 100.0) > self.approx_error: #verifying if current centroids have the same coordinates of previous centroids
					end = False #if there is no variation from previous centroids (centroids don't change their positions more than approx_error), set end to false

			if end:
				break

def main(path,n=3,approx_error=0.0000, iterations=500): #set arguments(n, approx_error, iterations) to default value if they're no passed
	
	
	data = pand.read_csv(path) #read the data source from the path argument
	data = data[['V1', 'V2']]  #V1 and V2 headers of the 'data' dataframe
	np_data = data.values #returns a numpy array
	
	km = K_Means_Alg(n, approx_error, iterations) #instantiate km of K_Means_Alg class
	km.exe(np_data) # perform the algorithm

	# Plotting the results
	print("Start Plotting..")
	colors = 30*["b", "r", "g", "c", "m", "y", "k"] #every cluster has its color

	for centroid in km.centroids:
		color = colors[centroid] #assign colors to centroid for plotting
		pyplt.scatter(km.centroids[centroid][0], km.centroids[centroid][1], c = color , s = 80, marker= "X") #plot centroids

	for pointclass in km.clusters:
		color = colors[pointclass] #assign colors to clusters for plotting
		for point in km.clusters[pointclass]:
			pyplt.scatter(point[0], point[1], color = color,s = 30, alpha= 0.4) #plot clusters
	pyplt.show()

if __name__ == "__main__":
	main(path='../dataset/k_means_clustering_test_1.csv', n=5) #set arguments for main function (path, n, approx_error, iterations)