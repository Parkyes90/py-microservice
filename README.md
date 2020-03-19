### Microservice

This project is for practicing microservices.


### Run
```shell script
git clone https://github.com/Parkyes90/py-microservice.git
cd py-microservice

pip install -r requirements.txt
FLASK_APP=services.app flask run
```


### Locust (Load Test)
```shell script
locust -f locust_script.py -- port 8080
```