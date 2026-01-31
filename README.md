# Functions_MLOps

[![Python application test with Github Actions](https://github.com/chungngoc/Functions_MLOps/actions/workflows/main.yml/badge.svg)](https://github.com/chungngoc/Functions_MLOps/actions/workflows/main.yml)


### To call microservice
Example : 
'''bash
curl -X 'POST' \
  'http://127.0.0.1:8080/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "facebook"
}'
'''

### Build container
'docker build .'
'docker image ls'

### Run container
Example : 
'docker run -p 127.0.0.1:8080:8080 9512cf97b076'

### Invoke
run 'invoke.sh'