## Letterify
a simple web api to extract letters from images, build with tesseract, flask and redis


### Usage:
1. Upload Image and query result
```
import requests
url = 'http://localhost:5000'
filepath = 'test.png'
# upload file using requests
with open(filepath, 'rb') as f:
    files = {'file': f}
    r = requests.post(url, files=files)
res = r.json
print(res)
key = res.['key']
# query results
url = 'http://localhost:5000/' + key
res = requests.get(url)
print(res.json) 
```

### Develop With Docker
#### Environment Setup
1. install docker and docker-compose
2. build docker image
`docker build . -t letterify`
3. docker-compose up


### Deploy
1. Enviroment Variable
* Set DEBUG to False in docker-compose.yml
2. Expose port 80


### TO DO
1. using celey to delay and distibute a image processing task
2. using a mock test db