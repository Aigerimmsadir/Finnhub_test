# Finnhub_test
# thenotebook

## SETUP:
Docker compose files are inside hidden .devcontainer folder. 
```bash
docker-compose build
docker-compose up
```
## API :
 
First you need to register 
**registration**:
 http://127.0.0.1:9009/users/  [POST]
 
   required fields:
      email, password

Then you will be able to log in
**login** :
http://127.0.0.1:9009/login/ [POST]

  required fields:: 
    email, password
    
   
You can subscribe to the news of the particular company. Choises: TSLA,NFLX,AMZN,BF,TWTR.

Authorization required
**subscribe** :
[[http://127.0.0.1:9009/subscribe/]][POST]

  required fields:: 
    ticket
  example:
  ```bash
{
   "ticket":"NFLX"
}
```

At any time tou can obtain all existing news of all companies. Authorization is not required.

**list all news** :

[[http://127.0.0.1:8000/companynews/]][POST]
    
