# Finnhub_test
# thenotebook

## SETUP:
Docker compose files are inside hidden .devcontainer folder. 
```bash
docker-compose build
docker-compose up
```
## API:

**registration**:
 http://127.0.0.1:9009/users/  [POST]
 
   required fields:
      username, email, password

**login** :
http://127.0.0.1:9009/login/ [POST]

  required fields:: 
    email, password
    



instagram_nickname


**update a notebook record**:

http://127.0.0.1:8000/records/<id>/ [PUT]


**delete a notebook record**:

http://127.0.0.1:8000/records/<id> [DELETE]
