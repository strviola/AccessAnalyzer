'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray
from analyze import point


if __name__ == '__main__':
    tikuwa_array = RequestArray('tikuwa_update')

    for t in tikuwa_array:
        p = point.make_point(t, 'tid', 'hasnum')
        print(p)
