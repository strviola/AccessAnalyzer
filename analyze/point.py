'''
Created on 2013/12/18

@author: SuzukiRyota
'''


from dateutil import parser


def get_time_from_login(request):
    '''
    Get user data from request (SimpleRequest class) and returns time from
    the user joined this app to posted.
    '''

    # get current time
    posted_str = request.user['last_login']
    posted = parser.parse(posted_str)
    # get user login date
    joined_str = request.user['date_joined']
    joined = parser.parse(joined_str)
    # calculate time delta
    return posted - joined


def make_point(request, *keys):
    '''
    Get Euclid point as list from SimpleRequest.
    This list always contains time from request-user-join to now.
    '''

    # first axis: user-join time to current time
    time_delta = get_time_from_login(request)
    delta_int = time_delta.total_seconds()
    # second~ axis: requested parameter as integer
    req = [int(request.REQUEST[key]) for key in keys]
    point = [delta_int]
    point.extend(req)

    return point


def make_unique(array):
    '''
    Remove duplicate elements in array.
    '''

    unique = []
    for item in array:
        if item not in unique:
            unique.append(item)
    return unique


def make_point_array_with_labels(request_array, *keys):
    # make points array
    point_array = [make_point(request, *keys) for request in request_array]
    # make true labels array
    label_array = [(1 if 'test' in request.REQUEST else 0)
                   for request in request_array]
    return point_array, label_array
