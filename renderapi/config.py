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
            "single": "/services/{}",
            "envvars": "/services/{}/env-vars",
            "headers": "/services/{}/headers",
            "routes": "/services/{}/routes",
            "suspend": "/services/{}/suspend",
            "resume": "/services/{}/resume",
            "scale": "/services/{}/scale",
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
