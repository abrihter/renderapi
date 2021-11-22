# render.com API wrapper

## Documentation
[render.com API documentation](https://apidocs.preview.render.com/)

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

```
