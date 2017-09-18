# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 08:00:06 2017

@author: Asanka
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def load_dataset(name):
    return np.loadtxt(name)


def euclidian(a, b):
    return np.linalg.norm(a-b)

def kmeans(k, epsilon=0, distance='euclidian'): #epsilon- minimumvalue to be used in stop condition 
    history_centroids = []
    
    if distance == 'euclidian':
        dist_method = euclidian
    dataset = load_dataset('dataset.txt')
    
    
    # dataset = dataset[:, 0:dataset.shape[1] - 1]
    num_instances, num_features = dataset.shape #rows instances and columns features
    prototypes = dataset[np.random.randint(0, num_instances - 1, size=k)]#decide centroids
    
    history_centroids.append(prototypes)#keep copy of centroids history
    
    prototypes_old = np.zeros(prototypes.shape) #empty vector atfirst keep track of centroids every interaction
    
    belongs_to = np.zeros((num_instances, 1)) #store clustors - data points belong here
    norm = dist_method(prototypes, prototypes_old) #distance between prototypes vs prototypes_old 
   

