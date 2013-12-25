'''
Created on 2013/12/22

@author: SuzukiRyota
'''


from util.request_logging import RequestArray
from analyze import point


if __name__ == '__main__':
    tikuwa_array = RequestArray('give_bonus')
    print('Before: %d' % len(tikuwa_array))

    i = 0
    for t in tikuwa_array:
        if (t.user['gmail'] == 'nirvana.kurt.940405@gmail.com' and
            t.REQUEST['money'] == '0' and t.REQUEST['uid'] == '10'):
            del tikuwa_array[i]
        i += 1

    print('After: %d' % len(tikuwa_array))
    for t in tikuwa_array:
        p = point.make_point(t, 'money', 'uid')
        print(p)

    tikuwa_array.close()
