'''
services resource
'''

import logging

from renderapi.base_resource import BaseResource

class Deploys(BaseResource):
    '''deploys resource'''

    def get(self, serviceId, deployId=None, limit=20, cursor=None):
        '''get deploys data

        :param str serviceId: Service ID
        :param str deployId: Deploy ID
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['deploys']['root']
        if deployId:
            path = self.config.API_ENDPOINTS['deploys']['single']
            path_vars.append(deployId)
        return self.make_request(
            'get',
            path,
            path_vars=path_vars,
            limit=limit,
            cursor=cursor
        )

    def trigger(self, serviceId, clearCache=False):
        '''trigger deploy

        :param str serviceId: Service ID
        :param str deployId: Deploy ID
        :param bool clearCache: If we want to clear cache
        :return object: Returns requests object
        '''
        clear_cache = 'do_not_clear'
        if clearCache:
            clear_cache = 'clear'
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['deploys']['root']
        data = {
            "clearCache": clear_cache,
        }
        return self.make_request(
            'post',
            path,
            path_vars=path_vars,
            request_json=data,
        )
