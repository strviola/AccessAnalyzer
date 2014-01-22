'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray
from analyze import point, cluster


if __name__ == '__main__':
    cheat_type = 'mid'
    tikuwa_cheat = RequestArray('tikuwa_update_cheat_%s' % cheat_type)
    tikuwa_array = []
    for filename in ['12_24', '12_25', '12_29', '12_30']:
        tikuwa_array.extend(RequestArray('tikuwa_update_%s' % filename))
    # tikuwa_array.extend(tikuwa_cheat)
    
    points, labels = point.make_point_array_with_labels(tikuwa_array, 'tid', 'hasnum')
    points_n, mean, var = point.normalize(points)
    print('Number of points: %d' % len(points))
    print('Means and standard deviations')
    for m, v in zip(mean, var):
        print(m, v)

    for eps in point.frange(0.5, 5, 0.5):
        for minpts in range(10, 20, 1):
            cluster_result, n_noise = cluster.dbscan(points_n, eps, minpts)
            
            print('Noises at eps=%f, minpts=%d: %d' % (eps, minpts, n_noise))
