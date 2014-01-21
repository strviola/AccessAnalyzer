'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray
from analyze import point, cluster


if __name__ == '__main__':
    tikuwa_cheat = RequestArray('tikuwa_update_cheat_mid')
    tikuwa_old = RequestArray('tikuwa_update_12_24')
    tikuwa_array = RequestArray('tikuwa_update_12_29')
    tikuwa_array.extend(tikuwa_old)
    # tikuwa_array.extend(tikuwa_cheat)
    
    points, labels = point.make_point_array_with_labels(tikuwa_array, 'tid', 'hasnum')
    points_n, mean, var = point.normalize(points)
    print('Number of points: %d' % len(points))
    print('Means and standard deviations')
    for m, v in zip(mean, var):
        print(m, v)
    # labels_est = cluster.dbscan(points).labels_
    
    for p, pn in zip(points, points_n):
        print(p, pn)
