import requests
import lxml.html
import pprint

from delete_database_entries import *

pp = pprint.PrettyPrinter(indent=4)

s= requests.Session()

# login = s.get('http://localhost:8000/auth/login/?next=/sessions/')
# login_html = lxml.html.fromstring(login.text)
# hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')

# form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
# form['username'] = "ben"
# form['password'] = "benben1234"

# print()
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Cookie and sessions information: "))
# print('{:*^50}'.format(""))
# pp.pprint(form)
# print('Got cookie? {}'.format(s.cookies == s.cookies))

# response = s.post('http://localhost:8000/auth/login/', data=form)
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Logging in: "))
# print('{:*^50}'.format(""))
# print('Response to login: {}'.format(response.status_code))
# print('Redirecting to: {}'.format(response.url))


# response = s.get('http://localhost:8000/sessions/')
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Printing all session data"))
# print('{:*^50}'.format(""))
# pp.pprint(response.json())

# session_id = "1"
# response = s.get('http://localhost:8000/sessions/'+session_id+ '/')
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Printing session id="+session_id))
# print('{:*^50}'.format(""))
# pp.pprint(response.json())



# response = s.get('http://localhost:8000/pipelineconfigurations/')
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Printing all PipelineConfiguration data"))
# print('{:*^50}'.format(""))
# pp.pprint(response.json())



# plconf_id = "1"
# response = s.get('http://localhost:8000/pipelineconfigurations/'+plconf_id+ '/')
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Printing PipelineConfiguration id="+session_id))
# print('{:*^50}'.format(""))
# pp.pprint(response.json())

# s.close()


# Clean up database
delete_models("observations")
delete_models("sessions")
delete_models("pipelineconfigurations")


obs_name = "pipodeclouwnnebula"
pipelineconf_name = "pipeline setup for clown nebula"


with requests.Session() as s:

	response = s.post('http://localhost:8000/observations/', data={"name": obs_name, "some_identifier": "a catalogue number of some kind"})
	print('{:*^50}'.format(""))
	print('{:*^50}'.format("Posting an observation"))
	print('{:*^50}'.format(""))
	print("Response code: ", response.status_code)
	pp.pprint(response.json())
	obs_id = response.json()["id"]

	response = s.post('http://localhost:8000/pipelineconfigurations/', data={"name": pipelineconf_name, "some_setting_1": 1.5, "some_setting_2": 3.6 })
	print('{:*^50}'.format(""))
	print('{:*^50}'.format("Posting a pipelineconfiguration"))
	print('{:*^50}'.format(""))
	print("Response code: ", response.status_code)
	pp.pprint(response.json())
	pl_conf_id = response.json()["id"]


	response = s.post('http://localhost:8000/sessions/', data={"name": "run 1 for clown nebula", "observation": obs_id, "pipeline_conf": pl_conf_id })
	print('{:*^50}'.format(""))
	print('{:*^50}'.format("Posting a session"))
	print('{:*^50}'.format(""))
	print("Response code: ", response.status_code)
	pp.pprint(response.json())

# with requests.Session() as s:
# 	#s.rebuild_auth
# 	print('http://localhost:8000/observations/'+str(response.json()["id"])+'/')
# 	response = s.delete('http://localhost:8000/observations/'+str(response.json()["id"])+'/', data={})#, data={"id": response.json()["id"]})