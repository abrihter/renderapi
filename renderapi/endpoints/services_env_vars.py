'''
services resource
'''

from renderapi.base_resource import BaseResource

class ServicesEnvVars(BaseResource):
    '''services env vars resource'''

    def get(self, serviceId, deployId=None, limit=20, cursor=None):
        '''get services env vars data

        :param str serviceId: Service ID
        :param str deployId: Deploy ID
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['services']['envvars']
        return self.make_request(
            'get',
            path,
            path_vars=path_vars,
            limit=limit,
            cursor=cursor,
        )

    def update(self, serviceId, env_vars):
        '''update services env vars resource

        :param str serviceId: Service ID
        :param dict env_vars: Deploy ID
        :return object: Returns requests object
        '''
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['services']['envvars']
        return self.make_request(
            'put',
            path,
            path_vars=path_vars,
            request_json=env_vars,
        )
