# ______________________________DOCKER LOGIN__________________________________
# |$ service docker stop                                                      |
# |                                                                           |
# |$ rm ~/.docker/config.json                                                 |
# |                                                                           |
# |$ sudo service docker start                                                |
# |                                                                           |
# |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////|


#  ___________________________CREATING IMAGE__________________________________
# |$ docker pull docker.io/library/python:3.12.1                              |
# |                                                                           |
# |$ docker build --file Dockerfile -t django-docker .                        |
# |                                                                           |
# |$ docker build -t styop01/arfa-med:1.0 .                                   |
# |                                                                           |
# |\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////////////|


#  _____________________________DOCKER PUSH___________________________________
# |$ docker push styop01/arfa-med:1.0                                         |
# |                                                                           |
# |"styop01" - Namespace(user)                                                |
# |"arfa-med" - Repo's name and also images name                              |
# |"1.0" - Repo's Tag(version)                                                |
# |                                                                           |
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


#  _____________________________RUNNING IMAGE_________________________________
# |$ docker compose up                                                        |



#  _____________________________CREATING POD__________________________________
# |$ kubectl run arfa-medd --image=styop01/arfa-med:1.0 --port=80             |


#  _____________________________CHECKING PODS_________________________________
# |$ kubectl get pod                                                          |


#  ____________________________CREATING SERVICES______________________________
# |$ kubectl expose pod arfa-med --name=arfa-medsvc --port=80                 |



#  ____________________________CHECKING SERVICES______________________________
# |$ kubectl get svc                                                         |
# |$ kubectl delete svc <svc name>

#  _____________________________RUNNING SERVICES______________________________
# |$ kubectl port-forward service/arfa-medsvc 8000:80                         |


# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]