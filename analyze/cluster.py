'''
Created on 2013/12/26

@author: SuzukiRyota
'''


from sklearn import cluster
from sklearn.preprocessing import StandardScaler


def dbscan(raw_points, eps, minpts):
    points = StandardScaler().fit_transform(raw_points)

    dbscan = cluster.DBSCAN(eps=eps, min_samples=minpts)
    divided = dbscan.fit(points)
    labels = divided.labels_  # 'labels' is simple list
    
    n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    
    # count up noises
    n_noise = 0
    for l in labels:
        if l == -1:
            n_noise += 1

    return divided, n_clusters, n_noise


def count_false(points, labels_true, dbscan_result):
    labels_est = dbscan_result.labels_

    false_negative = 0
    false_positive = 0
    for p, l_true, l_est in zip(points, labels_true, labels_est):
        fp = [p, l_true, l_est]
        if l_true == -1 and l_est != -1:
            false_negative += 1
            print('N', fp)
        elif l_true != -1 and l_est == -1:
            false_positive += 1
            print('P', fp)

    print('False positive: %d (rate: %f)' %
          (false_positive, false_positive * 1.0 / len(points)))
    print('False negative: %d (rate: %f)' % 
          (false_negative, false_negative * 1.0 / len(points)))


def step_dbscan(point_list, eps_list, minpts_list,
                contain_cheat=True, labels_true=None):

    # When just one EPS or MINPTS given: convert 1-length list
    if not isinstance(eps_list, list):
        eps_list = [eps_list]
    if not isinstance(minpts_list, list):
        minpts_list = [minpts_list]

    for eps in eps_list:
        for minpts in minpts_list:
            # DBSCAN: count noise
            cluster_result, n_clusters, n_noise = dbscan(point_list, eps, minpts)
            print('Noises at eps=%f, minpts=%d: %d' % (eps, minpts, n_noise))

            if contain_cheat:
                count_false(point_list, labels_true, cluster_result)
