'''
Created on 2013/12/18

@author: SuzukiRyota
'''


from util.request_logging import RequestArray


def get_time_from_login(request):
    '''
    Get user data from request (SimpleRequest class) and returns time from
    the user joined this app to now.
    '''

    user = request.user
    print(user.date_joined)


if __name__ == '__main__':
    tikuwa_array = RequestArray('tikuwa_update')
    get_time_from_login(tikuwa_array[0])
