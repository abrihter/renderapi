'''
owners resource
'''

import logging

from renderapi.base_resource import BaseResource

class Owners(BaseResource):
    '''owners resource'''

    def get(self, ownerId=None):
        '''get owners data

        :param str ownerId: Owner ID
        :return object: Returns requests object
        '''
        path_vars = []
        path = self.config.API_ENDPOINTS['owners']['root']
        if ownerId:
            path = self.config.API_ENDPOINTS['owners']['root']
            path_vars = [ownerId]
        return self.make_request('get', path, path_vars=path_vars)
