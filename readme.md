# Readme for LOFAR pipeline REST Api
This is an experiment to see if we can make the LOFAR data more accessible.
This is a django REST api using the django rest_framework. 

## Get it working
* Download this repo
* Create a venv in which you want to do your things (using python3) or use conda
* Install django (e.g. pip install django)
* Install the rest_framework (e.g. pip install djangorestframework)
* Install all the pipelines (as of 27JUN18 this is: https://github.com/EOSC-LOFAR/LGPPP_LOFAR_pipeline)
* Navigate to the folder containing the manage.py
* Start your local host: python manage.py runserver
* You can now send http requests to the localhost:8000. For example in your browser: localhost:8000/sessions/

## Follow an example
Check out the jupyter notebook: example_for_lofar_pilot_REST_api.ipynb. 

## Current models in the api
* Session: a session that will run a pipeline on an observation
* A post of a session using the request package could look like this:
```python
	data = {
			"email": "pipo@popo.com",
			"description": "Add your description to figure out later what this is.",
			"pipeline" : "LGPPP_LOFAR_pipeline",
			"config": "{\"avg_freq_step\": 1, \"avg_time_step\": 1, \"do_demix\": 1, \"demix_freq_step\": 1, \"demix_time_step\": 1, \"demix_sources\": 1, \"select_NL\": 1,\"parset\": 1}",
			"observation": "an observation code",
			}
	response = s.post('http://localhost:8000/sessions/', data=data)
```