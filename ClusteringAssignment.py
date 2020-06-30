import collections
import sys
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
import math
import time
import scipy
from scipy.spatial.distance import cdist, pdist

def file_to_array(file_name):
    with open(file_name) as f:
        data = f.readlines()
    arr = []
    for d in data:
        li =[]
        li_sub = d.split()
        li.append(float(li_sub[1]))
        li.append(float(li_sub[2]))
        arr.append(li)
    X = np.array(arr,dtype=np.float64)
    return X,arr

def heirarchical_clustering(file_name):
    X, arr = file_to_array(file_name)
    print(X)
    np.set_printoptions(threshold=np.nan)
    Z = linkage(X, 'single')
    plt.figure(figsize=(25, 10))
    plt.title('DendroGram for Single Link')
    plt.xlabel('Sample')
    plt.ylabel('Distance')
    dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels

    )
    plt.show()
    #print(Z)
    #print(X)
    Hclustering = AgglomerativeClustering(n_clusters=4,
                                          affinity='euclidean', linkage='ward')
    Hclustering.fit(X)
    #print(Hclustering.labels_)
    plt.scatter(X[:, 0], X[:, 1], c=Hclustering.labels_)
    plt.title('Graph For SingleLink')
    plt.show()
    Z = linkage(X, 'complete')
    plt.figure(figsize=(25, 10))
    plt.title('DendroGram for Complete Link')
    plt.xlabel('Sample')
    plt.ylabel('Distance')
    dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels

    )
    plt.show()
    agl_means_cost(arr, Hclustering.labels_)
    Hclustering = AgglomerativeClustering(n_clusters=4,
                                          affinity='euclidean', linkage='complete')
    Hclustering.fit(X)
    #print(Hclustering.labels_)
    plt.scatter(X[:, 0], X[:, 1], c=Hclustering.labels_)
    plt.title('Graph for Complete Link')
    plt.show()
    agl_means_cost(arr, Hclustering.labels_)
    Hclustering = AgglomerativeClustering(n_clusters=4,
                                          affinity='euclidean', linkage='average')
    Hclustering.fit(X)
    print(Hclustering.labels_)
    plt.scatter(X[:, 0], X[:, 1], c=Hclustering.labels_)
    plt.title('Graph For Mean Link')
    plt.show()
    Z = linkage(X, 'average')
    plt.figure(figsize=(25, 10))
    plt.title('DendroGram for Mean Links')
    plt.xlabel('Sample')
    plt.ylabel('Distance')
    dendrogram(
        Z,
        leaf_rotation=90.,  # rotates the x axis labels
        leaf_font_size=8.,  # font size for the x axis labels

    )
    plt.show()

def agl_means_cost(arr,labels):
    print('test')


def gonzalez(file_name, cluster_number):
    X, arr = file_to_array(file_name)
    cluster_labels = [0] * 1040
    cluster_centers = [arr[0]] * cluster_number

    for i in range(1, cluster_number):
        M = 0
        c = cluster_centers[i]
        index = 0
        for j in range(len(arr)):
            if distance(arr[j], cluster_centers[cluster_labels[j]]) > M:
                M = distance(arr[j], cluster_centers[cluster_labels[j]])
                c = arr[j]
                cluster_centers[i] = c
        j = 0
        # print(arr)
        for j in range(len(arr)):
            if distance(arr[j], cluster_centers[cluster_labels[j]]) > distance(arr[j], c):
                cluster_labels[j] = i
                #plt.scatter(X[:,0], X[:,1], c=cluster_labels)
                #plt.show()
    plt.scatter(X[:, 0], X[:, 1], c=cluster_labels)
    # print(cluster_centers)
    plt.title('Graph for Gonzalez')
    plt.show()
    M = 0
    sum_dist = 0
    for j in range(len(arr)):
        dist = distance(arr[j], cluster_centers[cluster_labels[j]])
        if dist > M:
            M = dist
        dist = dist * dist
        sum_dist = sum_dist + dist
    sum_dist = sum_dist / 1040
    print('The 3-center cost max is', M)
    print('The 3-means cost max is', math.sqrt(sum_dist))
    return cluster_centers

def phi_c_x(centers, x):
    shortest_distance = sys.maxsize
    candidate_c = None

    for c in centers:
        distance_c_x = distance(c, x)
        if distance_c_x < shortest_distance:
            shortest_distance = distance_c_x
            candidate_c = c

    return candidate_c;

def get_centers_kmeans(points, k):
    centers = []

    center_1_index = np.random.randint(0, len(points))
    centers.append(points[0].tolist())

    # print(centers)

    for i in range(1, k):

        distance_array = []

        for point in points:
            distance_x = distance(point, phi_c_x(centers, point))
            distance_array.append(distance_x)

        sum_distance = np.sum(distance_array)
        distance_array = [distance / sum_distance for distance in distance_array]

        center_index = np.random.choice(len(points), 1, distance_array)

        centers.append(points[center_index[0]].tolist())

    return centers

def kmeans_plus(file_name, cluster_number):
    X,arr = file_to_array(file_name)
    y_vals =[]
    x_vals =[]
    list_centers=[]
    for i in range(150):
        x_vals.append(i+1)
        C = get_centers_kmeans(X, cluster_number)
        cluster_labels=[0]*1040
        new_cluster_centers = C
        for k in range(len(arr)):
            M=2**31-1
            for j in range(len(new_cluster_centers)):
              if distance(arr[k],new_cluster_centers[j]) < M:
                M = distance(arr[k],new_cluster_centers[j])
                cluster_labels[k]=j
        # print(cluster_labels)
        y_vals.append(means_cost(arr,new_cluster_centers,cluster_labels))
        list_centers.append(new_cluster_centers)
        # plt.scatter(X[:,0], X[:,1], c=cluster_labels)
        # plt.title('K Means++ Algorithm')
        # plt.show()
    sorted_data = np.sort(y_vals)
    temp = float(len(sorted_data)-1)
    yvals=np.arange(len(sorted_data))/temp
    plt.plot(sorted_data,yvals)
    plt.title('CDF of 3-means cost')
    plt.xlabel('3-means cost')
    plt.show()
    count =0
    center_1 =gonzalez(file_name, cluster_number)
    for center in list_centers:
        # print(center)
        # print(center_1)
        result = [x for x in center if not x in center_1]
        if(len(result)==0):
            count = count+1
    print('The fraction of time the centers are equal is', count/150)

def kmeans(file_name, cluster_number):
    X,arr = file_to_array(file_name)
    #print(np.array([X[0],X[1],X[2]],np.float64))
    kmeans = KMeans(n_clusters=cluster_number,n_init=1, init=np.array([X[0],X[1],X[2]],np.float64)).fit(X)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    plt.scatter(X[:,0], X[:,1], c=kmeans.labels_)
    plt.title('Lloyds with initial Cluster centers as indexes (1,2,3)')
    plt.show()
    #print(labels)
    print('1,2,3',centers)
    means_cost(arr,centers,labels)
    kmeans = KMeans(n_clusters=cluster_number,n_init=1, init=np.array(gonzalez(file_name, cluster_number),np.float64)).fit(X)
    labels = kmeans.labels_
    centers = kmeans.cluster_centers_
    plt.scatter(X[:,0], X[:,1], c=kmeans.labels_)
    plt.title('Lloyds with initial Cluster as(gonzalez output)')
    plt.show()
    #print(labels)
    print('gonzalez',centers)
    means_cost(arr,centers,labels)
    list_means_cost = []
    for i in range(0,150):
        kmeans = KMeans(n_clusters=cluster_number,init=np.array(get_centers_kmeans(X, cluster_number))).fit(X)
        labels = kmeans.labels_
        centers = kmeans.cluster_centers_
        # print('The K means Cluster Centers are',centers)
        list_means_cost.append(means_cost(arr,centers,labels))
    # list_means_cost.append(6.32249345980089 )
    # list_means_cost.append(6.32249345980089 )
    # print(list_means_cost)
    sorted_data = np.sort(list_means_cost)
    temp = float(len(sorted_data)-1)
    yvals=np.arange(len(sorted_data))/temp
    plt.plot(sorted_data,yvals)
    plt.title('CDF of 3-means cost with Kmeans++ output')
    plt.show()

def means_cost(arr,centers,labels):
    M=0
    sum_dist = 0
    for j in range(len(arr)):
            dist = distance(arr[j],centers[labels[j]])
            if  dist > M:
                M = dist
            dist = dist*dist
            sum_dist = sum_dist + dist
    sum_dist = sum_dist/len(arr)
    #print('The 3-center cost max is', M)
    #print('The 3-means cost max is', math.sqrt(sum_dist))
    return math.sqrt(sum_dist)

def initialize(X, K):
    C = [X[0].tolist()]
    for k in range(1, K):
        D2 = scipy.array([min([scipy.inner(c-x,c-x) for c in C]) for x in X])
        #print(D2)
        probs = D2/D2.sum()
        #print(D2.sum())
        cumprobs = probs.cumsum()
        r = scipy.rand()
        for j,p in enumerate(cumprobs):
            if r < p:
                i = j
                break
        C.append(X[i].tolist())
    print('The initialized array is', C)
    return C

def distance(a,b):
    size = len(a);
    sum = 0;
    for i in range(0, size):
        sum = sum + math.pow(a[i]-b[i],2)
    return math.sqrt(sum)


def high_dimensional(d):
    a = d/2+1
    fact = 0
    #if a == 2.5:
    #   fact = 1.33
    #else:
    #   fact = math.factorial(a-1)
    fact = math.gamma(a)
    x = math.pow(math.pi, d/2)
    result = x/fact
    result = math.pow(result, 1/d)
    # print('The expansion factor for d=' + str(d) +' is', 2/result)
    return 2/result


def expansion_factor():
    print('The expansion factor for d=2 is', high_dimensional(2))
    print('The expansion factor for d=3 is', high_dimensional(3))
    print('The expansion factor for d=4 is', high_dimensional(4))
    y = []
    x = []
    for i in range(1,100):
        if(i%2 == 0):
            continue
        y.append(high_dimensional(i))
        x.append(i)
    plt.plot(x,y)
    plt.title('Graph for expansion factor')
    plt.xlabel('d Values')
    plt.ylabel('Expansion factor')
    plt.show()

#heirarchical_clustering('C1.txt')
#gonzalez('C2.txt',3)
#kmeans_plus('C2.txt',3)
#kmeans('C2.txt',3)
# expansion_factor()