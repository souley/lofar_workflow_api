# Readme for LOFAR pipeline REST Api
This is an experiment to see if we can make the LOFAR data more accessible.
This is a django REST api using the django rest_framework. Please note this is for brainstorming only. The api now contains some mock models and parameters just to start a discussion.

## Get it working
* Download this repo
* Create a venv in which you want to do your things (using python3)
* Install django (e.g. pip install django)
* Install the rest_framework (e.g. pip install djangorestframework)
* Navigate to the folder containing the manage.py
* Start your local host: python manage.py runserver
* You can now send http requests to the localhost:8000. For example in your browser: localhost:8000/sessions/

## Follow an example
Check out the jupyter notebook: example_for_lofar_pilot_REST_api.ipynb. It does some "post", "get" and "deletes"

## Current models in the api
* Observation: a model for an observation object
* PipelineConfiguration: a model containing parameters for a specific pipeline
* Session: a session that can run a pipeline on an observation using a pipeline configuration