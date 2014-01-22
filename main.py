'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray, collect_sample_from_dir
from analyze import point, cluster


if __name__ == '__main__':
    # collect samples
    tikuwa_array = collect_sample_from_dir('logs')

    # collect cheat inputs
#     cheat_type = 'sparse'
#     cheat_array = RequestArray('tikuwa_update_cheat_%s' % cheat_type, 'logs_cheat')
#     print('Number of cheats: %d' % len(cheat_array))
#     tikuwa_array.extend(cheat_array)

    points, labels = point.make_point_array_with_labels(tikuwa_array, 'tid', 'hasnum')
    points_n, mean, var = point.normalize(points)
    print('Number of points: %d' % len(points))
    print('Means and standard deviations')
    for m, v in zip(mean, var):
        print(m, v)

    cluster.step_dbscan(points_n, point.frange(0.5, 3, 0.25), range(10, 20, 1),
                        contain_cheat=False)
