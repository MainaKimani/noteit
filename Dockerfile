# The first instruction is what image we want to base our container on
# Use an official Python runtime as a parent image
FROM python:3.9-slim-bullseye

EXPOSE 8000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first.
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# create root directory for our project in the container
RUN mkdir /noteit

# Set the working directory to /noteit
WORKDIR /noteit

# Copy the current directory contents into the container at /noteit
ADD . /noteit/

# Install any needed packages specified in requirements.txt
RUN python -m pip install -r requirements.txt && \
    adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /noteit 

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
USER appuser

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "noteit.wsgi"]






