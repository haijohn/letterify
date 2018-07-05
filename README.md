## Letterify
a simple web api to extract letters from images, build with tesseract, flask and redis, the backend is build with flask simple server. we use [tesseract](https://github.com/tesseract-ocr/tesseract) to extract letters from images, finally the result is saved to redis for further use.


### Usage:
1. Upload Image and query result
```python
import requests
url = 'http://localhost:5000/'
filepath = 'test.png'
# upload file using requests
with open(filepath, 'rb') as f:
    files = {'file': f}
    r = requests.post(url, files=files)
# get reponse
res = r.json()
print(res)
key = res['key']
# query results
url = 'http://localhost:5000/' + key
res = requests.get(url)
print(res.json()) 
```

### Develop With Docker
#### Environment Setup
1. install docker and docker-compose
2. build docker image, see Dockerfile for software requirements.
`docker build . -t letterify`
3. `docker-compose up -d` to start web and redis service 


### Tests
the tests are in the test directory. you can run test with command
`python -m unittest discover`

### Deploy
1. Environment Variable
  * Set DEBUG to False in docker-compose.yml
2. Expose port 80


### TO DO
1. using celey to delay and distibute a image processing task.
2. using a mock database to run tests.