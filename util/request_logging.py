'''
Created on 2013/12/15

@author: SuzukiRyota
'''


import pickle
import os
import logging


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SAVE_DIR = os.path.join(BASE_DIR, 'logs')


class SimpleRequest:
    '''
    Simplified WSGIRequest class for serialization.

    Members:
        user:
            User data who sent the request.
        REQUEST:
            Request parameter dictionary.
    '''

    def __init__(self, request):
        self.user = request.user.to_dict()
        self.REQUEST = request.REQUEST

    def __str__(self):
        return '%s %s' % (self.user, str(self.REQUEST))


class RequestArray:
    '''
    Save access information to outer file.
    
    Members:
        req_array:
            The requested parameter as dictionary.
    '''

    def __init__(self, filename):
        self.req_file = os.path.join(SAVE_DIR, filename)
        
        # open outer file
        self.req_array = None
        try:
            with open(self.req_file, 'rb') as req_read:
                self.req_array = pickle.load(req_read)

        except (IOError, EOFError):
            logging.warning('File not found or broken. Make new pickle file.')
            self.req_array = []
            if not os.path.exists(SAVE_DIR):
                os.mkdir(SAVE_DIR)

    def close(self):
        with open(self.req_file, 'ab') as req_write:
            pickle.dump(self.req_array, req_write)
    
    # functions as user_array
    def append(self, request):
        req_simple = SimpleRequest(request)
        self.req_array.append(req_simple)

    def __str__(self):
        req_str = ''
        for r in self.req_array:
            req_str += str(r)
        return 'File: %s, Requests: %s' % (
            self.req_file, req_str)

    # function as with-context
    def __enter__(self):
        if self.req_array is None:
            raise ValueError('Failed to generate instance')
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        self.close()

    # function as array
    def __getitem__(self, index):
        return self.req_array[index]


def save_to_outer(request, filename):
    '''
    Serialize raw HTTP (WSGI) request and save to outer file.
    The saved file can use from other module.
    '''

    with RequestArray(filename) as array:
        array.append(request)
