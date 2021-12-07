'''
owners resource
'''

from renderapi.base_resource import BaseResource

class Owners(BaseResource):
    '''owners resource'''

    def get(self, ownerId=None, limit=20, cursor=None):
        '''get owners data

        :param str ownerId: Owner ID
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path_vars = []
        path = self.config.API_ENDPOINTS['owners']['root']
        if ownerId:
            path = self.config.API_ENDPOINTS['owners']['single']
            path_vars = [ownerId]
        return self.make_request(
            'get',
            path,
            path_vars=path_vars,
            limit=limit,
            cursor=cursor
        )
