'''
custom domains resource
'''

import logging

from renderapi.renderapi.base_resource import BaseResource

class Jobs(BaseResource):
    '''jobs resource'''

    def get(self, serviceId, jobId=None):
        '''get jobs data'''
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['jobs']['root']
        if jobId:
            path = self.config.API_ENDPOINTS['jobs']['single']
            path_vars.append(jobId)
        return self.make_request('get', path, path_vars=path_vars)

    def add(self, serviceId):
        '''create job'''
        path = self.config.API_ENDPOINTS['jobs']['root']
        path_vars = [serviceId]
        data = {}
        return self.request.make_request(
            'post',
            path,
            path_vars=path_vars,
            request_json=data,
        )
