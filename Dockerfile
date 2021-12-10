FROM python:3.9.4

# Create the user that will run the app
RUN adduser --disabled-password --gecos '' ml-api-user

WORKDIR /opt/titanic_webapp

ARG PIP_EXTRA_INDEX_URL

# Install requirements
ADD ./ /opt/titanic_webapp
RUN pip install --upgrade pip
RUN pip install -r /opt/titanic_webapp/requirements.txt

RUN chmod +x /opt/titanic_webapp/run.sh
RUN chown -R ml-api-user:ml-api-user ./

USER ml-api-user

EXPOSE 8001

CMD ["bash", "./run.sh"]