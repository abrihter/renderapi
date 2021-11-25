'''
services resource
'''

import logging

from renderapi.exceptions import ServiceTypeException
from renderapi.base_resource import BaseResource
from renderapi.endpoints.services_env_vars import ServicesEnvVars

class Services(BaseResource):
    '''services resource'''

    service_type_list = [
        'static_site',
        'web_service',
        'private_service',
        'background_worker',
        'cron_job',
    ]

    def __init__(self, api_key):
        '''init'''
        super().__init__(api_key)

        self.env_vars = ServicesEnvVars(api_key)

    def get(self, serviceId=None, limit=20, cursor=None):
        '''get services data

        :param str serviceId: Service ID
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path_vars = None
        path = self.config.API_ENDPOINTS['services']['root']
        if serviceId:
            path = self.config.API_ENDPOINTS['services']['single']
            path_vars = [serviceId]
        return self.make_request(
            'get',
            path,
            limit=limit,
            cursor=cursor,
            path_vars=path_vars,
        )

    def add(self, service_type, name, ownerId, repo, serviceDetails={},
            autoDeploy=True, branch='', envVars=None, secretFiles=None):
        '''create services

        :params str service_type: Service type to create
        :param str name: Service name
        :param str ownerId: Owner ID
        :param str repo: Repo
        :param dict serviceDetails: Service details
        :param bool autoDeploy: Auto deploy
        :param str branch: If left empty, this will fall back to the
                            default branch of the repository
        :param list envVars: Env vars
        :param list secretFiles: Secret files
        :return object: Returns requests object
        '''
        if service_type not in self.service_type_list:
            logging.debug(
                'Service type `{}` is not valid, need to be one of {}'.format(
                    service_type, self.service_type_list))
            raise ServiceTypeException('Invalid service type')

        auto_deploy = 'no'
        if autoDeploy:
            auto_deploy = 'yes'
        path = self.config.API_ENDPOINTS['services']['root']
        data = {
            "type": service_type,
            "name": name,
            "ownerId": ownerId,
            "repo": repo,
            "autoDeploy": auto_deploy,
            "serviceDetails": serviceDetails,
        }
        if branch:
            data['branch'] = branch
        if envVars:
            data['envVars'] = envVars
        if secretFiles:
            data['secretFiles'] = secretFiles
        return self.make_request(
            'post',
            path,
            request_json=data,
        )

    def delete(self, serviceId):
        '''delete services

        :param str serviceId: Service ID
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['services']['single']
        path_vars = [serviceId]
        return self.make_request('delete', path, path_vars=path_vars)

    def update(self, serviceId, autoDeploy=None, name=None, branch=None,
            serviceDetails={}):
        '''update services

        :param str serviceId: Service ID
        :param bool autoDeploy: Auto deploy
        :param str name: Service name
        :param str branch: If left empty, this will fall back to the
                            default branch of the repository
        :param dict serviceDetails: Service details
        :return object: Returns requests object
        '''
        auto_deploy = None
        if autoDeploy != None:
            auto_deploy = 'no'
            if autoDeploy:
                auto_deploy = 'yes'
        path_vars = [serviceId]
        path = self.config.API_ENDPOINTS['services']['single']
        data = {
            "serviceDetails": serviceDetails,
        }
        if auto_deploy:
            data['autoDeploy'] = auto_deploy
        if name:
            data['name'] = name
        if branch:
            data['branch'] = branch
        return self.make_request(
            'patch',
            path,
            request_json=data,
            path_vars=path_vars,
        )

    def get_headers(self, serviceId, path=[], name=[], value=[], limit=20,
            cursor=None):
        '''get service headers data

        :param str serviceId: Service ID
        :param list path: Filter for specific paths that headers apply to
        :param list name: Filter for header names
        :param list value: Filter for header values
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path_uri = self.config.API_ENDPOINTS['services']['headers']
        path_vars = [serviceId]
        params = {}
        if path:
            params['path'] = ",".join(path)
        if name:
            params['name'] = ",".join(name)
        if value:
            params['value'] = ",".join(value)
        return self.make_request(
            'get',
            path_uri,
            limit=limit,
            cursor=cursor,
            path_vars=path_vars,
            params=params,
        )

    def get_routes(self, serviceId, route_type=[], source=[], destination=[],
            limit=20, cursor=None):
        '''get service routes

        :param str serviceId: Service ID
        :param list route_type: Filter for the type of route rule
        :param list source: Filter for the source path of the route
        :param list destination: Filter for the destination path of the route
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['services']['routes']
        path_vars = [serviceId]
        params = {}
        if route_type:
            params['route_type'] = ",".join(route_type)
        if source:
            params['source'] = ",".join(source)
        if destination:
            params['destination'] = ",".join(destination)
        return self.make_request(
            'get',
            path,
            limit=limit,
            cursor=cursor,
            path_vars=path_vars,
            params=params,
        )

    def suspend(self, serviceId):
        '''service suspend

        :param str serviceId: Service ID
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['services']['suspend']
        path_vars = [serviceId]
        return self.make_request(
            'post',
            path,
            path_vars=path_vars,
        )

    def resume(self, serviceId):
        '''service resume

        :param str serviceId: Service ID
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['services']['resume']
        path_vars = [serviceId]
        return self.make_request(
            'post',
            path,
            path_vars=path_vars,
        )

    def scale(self, serviceId, numInstances):
        '''service scale

        :param str serviceId: Service ID
        :param int numInstances: Number of instances
        :return object: Returns requests object
        '''
        path = self.config.API_ENDPOINTS['services']['scale']
        path_vars = [serviceId]
        data = {
            "numInstances": int(numInstances),
        }
        return self.make_request(
            'post',
            path,
            request_json=data,
            path_vars=path_vars,
        )
