'''
Created on 2013/12/26

@author: SuzukiRyota
'''


from sklearn import cluster
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler


def divide(points):
    points = StandardScaler().fit_transform(points)
    print(points)
    
    dbscan = cluster.DBSCAN(eps=2, min_samples=10)
    divided =dbscan.fit(points)
    labels = divided.labels_
    
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
    print('Estimated number of clusters: %d' % n_clusters)


if __name__ == '__main__':
    centers = [[1, 1], [-1, -1], [1, -1]]
    X, labels_true = make_blobs(n_samples=750, centers=centers, cluster_std=0.4,
                            random_state=0)

    X = StandardScaler().fit_transform(X)
    print(X)
    
    db = cluster.DBSCAN(eps=0.3, min_samples=10).fit(X)
    print(db)
