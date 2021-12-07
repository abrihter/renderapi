'''
custom domains resource
'''

from renderapi.base_resource import BaseResource

class Jobs(BaseResource):
    '''jobs resource'''

    def get(self, serviceId, jobId=None, limit=20, cursor=None):
        '''get jobs data

        :param str serviceId: Service ID
        :param str jobId: Job ID
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['jobs']['root']
        if jobId:
            path = self.config.API_ENDPOINTS['jobs']['single']
            path_vars.append(jobId)
        return self.make_request(
            'get',
            path,
            path_vars=path_vars,
            limit=limit,
            cusror=cursor,
        )

    def add(self, serviceId):
        '''create job

        :param str serviceId: Service ID
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['jobs']['root']
        path_vars = [serviceId]
        data = {}
        return self.make_request(
            'post',
            path,
            path_vars=path_vars,
            request_json=data,
        )
