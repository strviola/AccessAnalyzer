'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray
from analyze import point, cluster


if __name__ == '__main__':
    tikuwa_old = RequestArray('tikuwa_update_12_24')
    tikuwa_array = RequestArray('tikuwa_update')
    tikuwa_array.extend(tikuwa_old)
    
    points = [point.make_point(t, 'tid', 'hasnum') for t in tikuwa_array]
    print('Number of points: %d' % len(points))
    cluster.divide(points)
