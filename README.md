# Titanic webapp
The application is built using FastAPI framework. 
It has been uploaded to Heroku service and is available via the link: https://titanicwebapp.herokuapp.com/.

## How to run the app
The app can be run locally via the [Tox](https://pypi.org/project/tox/) tool. In order to run the app 
clone the repo, install Tox and run `tox -e run_app`. You can also test the app and run linters with the commands
`tox -e test_app` and `tox -e lint` correspondingly.

## Docker
The possibility to run the app via the docker container has been added. 
In order to do that first build the docker image using the Dockerfile:

`docker build --build-arg 
PIP_EXTRA_INDEX_URL=https://pypi.org/project/titanic-model/ -t titanic_model:latest .`

After that the app can be run with the following command:

`docker run -p 8001:8001 -e PORT=8001 titanic_model`