'''
custom domains resource
'''

import logging

from renderapi.renderapi.base_resource import BaseResource

class CustomDomains(BaseResource):
    '''custom domains resource'''

    def get(self, serviceId, customDomainIdOrName=None):
        '''get custom domains data'''
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['custom_domains']['root']
        if customDomainIdOrName:
            path = self.config.API_ENDPOINTS['custom_domains']['name']
            path_vars.append(customDomainIdOrName)
        return self.make_request('get', path, path_vars=path_vars)

    def get_domain(self, serviceId, customDomainIdOrName):
        '''get particular custom domain data'''
        path = self.config.API_ENDPOINTS['custom_domains']['name']
        path_vars = [serviceId, customDomainIdOrName]
        return self.make_request('get', path, path_vars=path_vars)

    def add(self, serviceId):
        '''create custom domains'''
        path = self.config.API_ENDPOINTS['custom_domains']['root']
        path_vars = [serviceId]
        data = {}
        return self.request.make_request(
            'post',
            path,
            path_vars=path_vars,
            request_json=data,
        )

    def delete(self, serviceId, customDomainIdOrName):
        '''delete custom domains'''
        path = self.config.API_ENDPOINTS['custom_domains']['name']
        path_vars = [serviceId, customDomainIdOrName]
        return self.make_request('delete', path, path_vars=path_vars)

    def verify(self, serviceId, customDomainIdOrName):
        '''get custom gomains verify data'''
        path = self.config.API_ENDPOINTS['custom_domains']['verify']
        path_vars = [serviceId, customDomainIdOrName]
        return self.make_request('post', path, path_vars=path_vars)
