'''
services resource
'''

import logging

from renderapi.base_resource import BaseResource

class Services(BaseResource):
    '''services resource'''

    def get(self, limit=20, cursor=None):
        '''get services data

        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['services']['root']
        return self.make_request(
            'get',
            path,
            limit=limit,
            cursor=cursor
        )
