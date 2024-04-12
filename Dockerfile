#  ___________________________CREATING IMAGE__________________________________
# |docker build --file Dockerfile -t django-docker .                          |


#  ____________________________RUNNING IMAGE__________________________________
# |docker compose up                                                          |



# Use an official Python runtime as a parent image
FROM python:3.12.1

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]