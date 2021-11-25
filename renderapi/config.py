'''
config
'''

class Config:
    '''configuration class'''

    API_BASE_URL = 'https://api.render.com/v1'

    API_ENDPOINTS = {
        "owners": {
            'root': '/owners',
            'single': '/owners/{}',
        },
        "services": {
            "root": "/services",
        },
        "deploys": {
            "root": "/services/{}/deploys",
            "single": "/services/{}/deploys/{}",
        },
        "custom_domains": {
            "root": "/services/{}/custom-domains",
            "name": "/services/{}/custom-domains/{}",
            "verify": "/services/{}/custom-domains/{}/verify",
        },
        "jobs": {
            "root": "/services/{}/jobs",
            "single": "/services/{}/jobs/{}",
        }
    }
