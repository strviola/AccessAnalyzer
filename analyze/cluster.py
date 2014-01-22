'''
Created on 2013/12/26

@author: SuzukiRyota
'''


from sklearn import cluster
from sklearn.preprocessing import StandardScaler


def dbscan(raw_points, eps, minpts):
    points = StandardScaler().fit_transform(raw_points)

    dbscan = cluster.DBSCAN(eps=eps, min_samples=minpts)
    divided =dbscan.fit(points)
    labels = divided.labels_  # 'labels' is simple list
    
    n_clusters = len(set(labels))
    
    # count up noises
    n_noise = 0
    for l in labels:
        if l == -1:
            n_noise += 1

    print('Estimated number of clusters: %d' % n_clusters)
    return divided, n_noise
