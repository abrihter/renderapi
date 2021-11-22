'''
render.com API wrapper
'''

__author__ = "Bojan"
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Bojan"
__status__ = "Production"

import logging

from renderapi.exceptions import InvalidKeyException
from renderapi.owners import Owners
from renderapi.custom_domains import CustomDomains
from renderapi.jobs import Jobs

class RenderApi:
    '''render API main class'''

    def __init__(self, api_key=None):
        '''init'''

        self.api_key = api_key

        if not self.api_key:
            logging.debug('API key not present []'.format(self.api_key))
            raise InvalidKeyException('Empty key provided')

        self.owners = Owners(self.api_key)
        self.custom_domains = CustomDomains(self.api_key)
        self.jobs = Jobs(self.api_key)
