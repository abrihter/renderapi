# render.com API wrapper

## Documentation
[render.com API documentation](https://render-api.readme.io/reference/introduction)

## Coverage
Aiming for full coverage. Currently we should support full functionality of render.com API
___
## Install
```pip install renderapi```
___

### How to use
```python
from renderapi import RenderApi

ra = RenderApi({RENDER_API_KEY})

#get custom domains
data = ra.custom_domains.get({serviceId})
print(data)
print(data.json())

#get jobs
data = ra.jobs.get({serviceId})
print(data)
print(data.json())

#get owners
data = ra.owners.get({ownerId})
print(data)
print(data.json())

#get services
data = ra.services.get()
print(data)
print(data.json())

#get deploys
data = ra.deploys.get({serviceId})
print(data)
print(data.json())

```
