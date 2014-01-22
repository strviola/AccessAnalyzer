'''
Created on 2014/01/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray, collect_sample_from_dir
from analyze import cluster, point


if __name__ == '__main__':
    tikuwa_array = collect_sample_from_dir('logs')

    # insert cheats
    cheat_type = 'dens'
    cheat_array = RequestArray('tikuwa_update_cheat_%s' % cheat_type,
                               'logs_cheat')
    tikuwa_array.extend(cheat_array)

    # step DBSCAN analyze
    points, labels = point.make_point_array_with_labels(tikuwa_array,
                                                        'tid', 'hasnum')
    points_n, mean, var = point.normalize(points)
    print('Number of points: %d' % len(points))
    print('Means and standard deviations')
    for m, v in zip(mean, var):
        print(m, v)

    cluster.step_dbscan(points_n, point.frange(0.5, 1.6, 0.1), range(9, 15, 1),
                        contain_cheat=True, labels_true=labels, latex=True)
