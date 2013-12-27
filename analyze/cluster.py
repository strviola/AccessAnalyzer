'''
Created on 2013/12/26

@author: SuzukiRyota
'''


from sklearn import cluster
from sklearn.preprocessing import StandardScaler


def dbscan(raw_points):
    points = StandardScaler().fit_transform(raw_points)

    dbscan = cluster.DBSCAN(eps=1.2, min_samples=20)
    divided =dbscan.fit(points)
    labels = divided.labels_  # 'labels' is simple list
    
    n_clusters = len(set(labels))
    
    print('Estimated number of clusters: %d' % n_clusters)
    return divided
