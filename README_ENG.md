# K-Means Clustering

Final essay about the course: INTERNET OF THINGS BASED SMART SYSTEMS - UniCT.

This Tool implements [K-means clustering algorithm](https://en.wikipedia.org/wiki/K-means_clustering#Algorithms) a precise or approximate version. The degree of approximation is introduced through the parameters supplied at the input of the script (approx_factor, max_iterations). This allows to implement the 'loop perforation' technique of Approximate Computing.

The structure of the repository is as follows:
-	**Dataset**: it contains the files .cvs  used as data source for the computation (the structure of these files will be described in the appropriate section).
-	**Src**: it contains the source code of the .py application.
-	**Output**: it contains the cluster.pdf file who represents the plot of the clustering results, the _ReadableResults.csv_ file representing the output of the algorithm execution in readable format, the _results.csv_ file representing the output of the algorithm execution in raw format, usable for DNN computation.

This tool can be used as an approximate kernel in DNNs that base themselves on data clustering for implementations in limited resource devices.

## Dependencies

The tool has been implemented in python (it is assumed that python3 and pip3 have already been installed; otherwise download).
For a correct execution it is necessary to install the following modules:
- **pandas**
- **numpy**
- **matplotlib**
- **scipy**

Dependencies installation must be done using the following commands:

```[shell]
pip3 install pandas
pip3 install numpy
pip3 install matplotlib
pip3 install scipy

```
## Input File structure

The input data for the computation must be placed in the directory dataset. These data must be provided as a .csv file (the _test1.csv_, _test2.csv_ files are provided for testing purposes). This file must be provided as an input parameter when the script is run.

In the case of files with two-dimensional datasets, the file must have the following headers for the columns: **V1**, **V2**.

In the case of files with one-dimensional dataset, the file must have the following header for the column: **V1**.

For the cases described above, the tool provides full support for printing the results. In the case of n-dimensional datasets (with n> 2), printing is performed only in the 2 dimensions x and y.

The structure of the n-dimensional files must follow the convention for headers described above: **V1**,..,**Vn**

## Output File Structure 

The output file in raw format (results.csv) provides useful information at the end of the computation. This essential information is the Codebook and the cluster-indexes relating to all points of the dataset. 

The Codebook is represented by the indices relating to the centroids that define the clusters and the coordinates of the centroids themselves. The cluster-index relating to the points define which cluster they belong to. 

This guarantees us a compression factor of **32/log2(k)**, so we represent the information relating to the points only through the coding of the cluster index, rather than a 32-bit float. 

In the _results.csv_ file, the indexes and coordinates of the centroids are first represented and then, for each point of the dataset, the index of its cluster is followed.

## Start

To start the tool type the following commands (valid for both bash linux and powershell windows) in the main directory :

```[python]
cd ./src
python3 k-means_approx.py

```
After the launch 4 parameters are required  :

- **Enter cluster size**: it requires to insert an integer value that represents the size of the cluster.
- **Enter approximation factor 0 < appr_factor < 1 :** it requires to insert a float value between 0 and 1 which represents the approximation factor.
- **Enter MAX iteration number**: it requires the maximum value of the iterations potentially executable by the algorithm (it could converge with fewer iterations).
- **Enter input file name ( .csv )**: it requires the name of the input .csv file present in the dataset.
- **Do you want to visualize the result? ( yes or no )**: it requires typing "yes" to display the plot of results dynamically at the end of execution. 

## Example

Execution example with the following parameters:
- cluster size = 5
- approximation_factor = 0.002
- max iter = 50
- input file = test2.csv (two-dimensional dataset)

the result of the execution is represented by the following image:

![simulation result](https://github.com/RaiMar96/IoT_project_2k19-20/blob/master/example/example-bi.png)

Execution example with the following parameters:
- cluster size = 5
- approximation_factor = 0.002
- max iter = 50
- input file = test1.csv (one-dimensional dataset)

the result of the execution is represented by the following image:

![simulation result](https://github.com/RaiMar96/IoT_project_2k19-20/blob/master/example/example-mono.png)




