'''
custom requests
'''

import requests
import logging
from renderapi.renderapi.config import Config

class Request:
    '''request class'''

    def __init__(self, api_key):
        '''init'''
        self.api_key = api_key

        if not self.api_key:
            raise InvalidKeyException('Empty key provided')

    def make_request(self, method, path, request_json=None):
        '''make request'''
        s = requests.Session()
        s.headers.update({'Authorization': 'Bearer {}'.format(self.api_key)})
        data = None
        if method == 'get':
            data = s.get(path)
        elif method == 'post':
            data = s.post(path, json=request_json)
        elif method == 'delete':
            data = s.delete(path)
        logging.debug(data.content)
        return data

