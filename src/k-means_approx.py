#K-Means approximated Implementaion:
#Raiti Mario O55000434
#Nardo Gabriele Salvatore O55000430

# Precise Version --> approx_error = 0.0000 ( default value ) 
# Approximated Version --> approx_error > 0.0000 , choose iterations < default iter

#A CSV file containig all the point to process is used as input

import random
from scipy.spatial import distance
import csv
import pandas as pand
import numpy as nump
import matplotlib.pyplot as pyplt
from matplotlib import style
import random as rd

style.use('ggplot')

class K_Means_Alg: 	#class K-Means_Alg define attributes and methods to perform the algorithm
	def __init__(self, n, approx_error, iterations):
		self.approx_error = approx_error				#set the approx factor
		self.iterations = iterations    				#set the number of iterations
		self.n = n 										#set the number of clusters/centroids
		
	def exe(self, data):   #exe method perform the algorithm

		self.centroids = {} #initialize dictionary to save centroids coordinates
		
		#this solution select random centroids from the dataset
		#for i in range(self.n):
			#self.centroids[i] = data[(random.randint(0, len(data)))]      

		for i in range(self.n):
			self.centroids[i] = data[i] #this solution select the firsts dataset elements as centroids

		#iterations
		for it in range(self.iterations):
			self.clusters = {} #initialize clusters dictionary
			for i in range(self.n):
				self.clusters[i] = [] #initialize a list for every cluster(number of centroids -> n)

			#choose the nearest centroid based on the distance from the point
			for point in data:
				distances = [distance.euclidean(point , self.centroids[centroid]) for centroid in self.centroids] #'distances' store the euclidean distances from the point to each centroids
				pointclass = distances.index(min(distances)) #'pointclass' store for each point, the index of the cluster based on the min distance from each centroid
				self.clusters[pointclass].append(point) #append each point to its cluster (clusters[pointclass] where pointclass is the index that identify the cluster)

			previous = dict(self.centroids) #store centroids to compare them later to new re-calculated centroids

			#average the cluster datapoints to re-calculate the centroids
			for pointclass in self.clusters:
				if self.clusters[pointclass]: self.centroids[pointclass] = nump.average(self.clusters[pointclass], axis = 0) #centroids[] now contains the coordinates of the new recalculated centroids. The if instruction verify that the cluster is not empty. If cluster is empty, centroid don't change coordinates

			end = True #end is used to verify if the algorithm has converged
			print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
			print("\nIteration: " +str(it+1)) #print current iteration
			print("Normalized coordinates of new centroids:")
			for centroid in self.centroids: #for each centroid, 'original centroid' contain its previous coordinates, whereas 'curr' contain its current coordinates
				original_centroid = previous[centroid]
				curr = self.centroids[centroid]
				print(nump.sum(distance.euclidean(curr,original_centroid)/original_centroid))

				if nump.sum(distance.euclidean(curr,original_centroid)/original_centroid) > self.approx_error: #verifying if current centroids have the same coordinates of previous centroids
					end = False #if there is no variation from previous centroids (centroids don't change their positions more than approx_error), set end to false
			if end:
				print("Final iteration: "+str(it+1)) #this statement print the final iteration if the algorithm has converged before the max number of iterations
				print("Algorithm has converged with approximation error of: " + str(self.approx_error))
				break
			if (it == (self.iterations-1)):
				print("Final iteration: "+str(it+1)) #this statement print the final iteration if the algorithm reach the max number of iterations
				print("Max iterations reached. Needs more iterations to converge")

def main():
	# interaction with the user to define the execution parameters
	cluster_size = int(input("Enter cluster size : "))
	appr_factor = float(input("Enter approximation factor 0 < appr_factor < 1 : "))
	cicles = int(input("Enter MAX iterations number executable : "))
	input_file = input("Enter input file name ( .csv ) : ")
	show = input("Do you want to visualize the result? ( yes or no ) : ")

	path='../dataset/'+input_file #set the path for the input dataset

	with open(path, "r") as f:
		reader = csv.reader(f)
		i = next(reader) #'i' is an array containing the headers of the csv file; is useful later for plotting different dataset (monodimensional o bidimensional)
	
	data = pand.read_csv(path) #read the data source from the path argument
	np_data = data.values #returns a numpy array
	
	km = K_Means_Alg(cluster_size, appr_factor, cicles) #instantiate km of K_Means_Alg class
	km.exe(np_data) # perform the algorithm

	# Plotting the results
	print("Start Plotting..")
	colors = ["b", "r", "g", "c", "m", "y", "k"] #every cluster has its color. The firsts 7 colors for the firsts 7 clusters are fixed: blue, red, green, ciano, magenta, yellow and black

	#this code block is used to assign different colors dinamically for each clusters fìafter the 7th cluster. 
	l = len(km.centroids)
	if l > len(colors):
		l2 = l - len(colors)
		for x in range(l2): #l2 is the number of the clusters after the 7th cluster
			randint = rd.randint(1048576,16777215)
			rcolor = hex(randint) #hex() convert the randint value in hexadecimal. The generated hexadecimal value is in the range 100000 to FFFFFF
			colors.append('#'+str(rcolor[2:])) #append the color to the colors list

	
	subplt = pyplt.subplot()
	pyplt.title('K-Means Clusters Results - Approx error : ' + str(appr_factor)) 


	for centroid in km.centroids:
		color = colors[centroid] #assign colors to centroid for plotting
		if(len(i) == 1 ):
			y = 0
		else : y = km.centroids[centroid][1]
		subplt.scatter(km.centroids[centroid][0], y,  c = color , s = 80, marker= "X", label='Cluster '+str(centroid)) #plot centroids. If len(i)==1, the point has one coordinate, so set y=0

	for pointclass in km.clusters:
		color = colors[pointclass] #assign colors to clusters for plotting
		for point in km.clusters[pointclass]:
			if(len(i) == 1 ): #setting the y coordinate for mono or bi dimenisional version 
				y = 0
			else : y = point[1]
			subplt.scatter(point[0], y, color = color,s = 30, alpha= 0.4) #plot clusters

	chartBox = subplt.get_position()
	subplt.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.85, chartBox.height]) #set the new subplot position based on its original position
	subplt.legend(loc="upper left", bbox_to_anchor=(1.0, 1.0), shadow=True) #add legend
	pyplt.savefig('../output/cluster.pdf', bbox_inches='tight') #save a result png
	print("Result saved in the Output directory")
	if(show == 'yes'):
		pyplt.show()

if __name__ == "__main__":
	main()