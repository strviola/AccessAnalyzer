'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray
from analyze import point, cluster


if __name__ == '__main__':
    tikuwa_cheat = RequestArray('tikuwa_update_cheat')
    tikuwa_old = RequestArray('tikuwa_update_12_24')
    tikuwa_array = RequestArray('tikuwa_update')
    tikuwa_array.extend(tikuwa_old)
    tikuwa_array.extend(tikuwa_cheat)
    
    points, labels = point.make_point_array_with_labels(tikuwa_array, 'tid', 'hasnum')
    print('Number of points: %d' % len(points))
    labels_est = cluster.dbscan(points).labels_
    
    for p, l_true, l_est in zip(points, labels, labels_est):
        print(p, l_true, l_est)
