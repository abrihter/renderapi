'''
base resource
'''

import logging

from renderapi.custom_requests import Request
from renderapi.config import Config

class BaseResource:
    '''base resource'''

    def __init__(self, api_key):
        '''init

        :param str api_key: Render API key
        '''
        self.api_key = api_key

        if not self.api_key:
            raise InvalidKeyException('Empty key provided')

        self.request = Request(self.api_key)
        self.config = Config

    def __create_api_url(self, path):
        '''create URL for call

        :param str path: Path to format for
        '''
        return '{}{}'.format(Config.API_BASE_URL, path)

    def make_request(
        self, method, path_data, path_vars=[], request_json=None, limit=20,
            cursor=None):
        '''make request on resource

        :param str method: Method to use
        :param str path_data: Path data to format
        :param list path_vars: Path vars to update
        :param dict request_json: Request json data
        :param int limit: Return limit
        :param str cursor: Cursor for serarch (next)
        :return object: Returns requests object
        '''
        params = {
            "limit": limit,
            "cursor": cursor,
        }
        path = self.__create_api_url(path_data.format(*path_vars))
        logging.debug("render.com PATH {}".format(path))
        return self.request.make_request(
            method,
            path,
            request_json=request_json,
            params=params,
        )
