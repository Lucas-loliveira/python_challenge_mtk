# python-challenge: Transparency in Coverage
Author: Lucas da Silva de Oliveira (lucasoliveira783@gmail.com, https://www.linkedin.com/in/lucas-sil-oliveira)


Main technologies used:
  * python3
  * docker
  * docker-compose
  * flask
  * sqlite

Requirements
============
  * [docker](https://www.docker.com/)
  * [docker-compose](https://docs.docker.com/compose/)

How to run the app
============
run the containers
```bash
$ make build up
```
run the script that will download all files from https://transparency-in-coverage.uhc.com/ and save the results in the local database
```bash
$ make create data
```
The script takes about 2h to finish, the progress can be followed in the terminal. The process can also be terminated at any time and progress will not be lost. however, when running the script again, the data will be inserted in the database again.

### curl example to use search api based on company name

```
curl --request GET \
  --url http://localhost:5000/search \
  --header 'Content-Type: application/json' \
  --data '{
	"method":"name",
	"query":"United Healthcare POS"
}'
```


### curl example to use search api based on company EIN

```
curl --request GET \
  --url http://localhost:5000/search \
  --header 'Content-Type: application/json' \
  --data '{
	"method":"ein",
	"query":"841556137"
}'
```


Future improvements
=====
  * Use a swagger or any other documentation tool
  * Perform multiple asynchronous requests to dowload the employer specific files
  * Replace prints with logs
  * Create a "time to live" policy, thus updating the database data periodically
  * Different environment variables for dev and production environments
  * Automated tests

