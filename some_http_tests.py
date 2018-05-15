import requests
import lxml.html
import pprint

pp = pprint.PrettyPrinter(indent=4)

s= requests.Session()

login = s.get('http://localhost:8000/auth/login/?next=/sessions/')
login_html = lxml.html.fromstring(login.text)
hidden_inputs = login_html.xpath(r'//form//input[@type="hidden"]')

form = {x.attrib["name"]: x.attrib["value"] for x in hidden_inputs}
form['username'] = "ben"
form['password'] = "benben1234"

print()
print('{:*^50}'.format(""))
print('{:*^50}'.format("Cookie and sessions information: "))
print('{:*^50}'.format(""))
pp.pprint(form)
print('Got cookie? {}'.format(s.cookies == s.cookies))

# response = s.post('http://localhost:8000/auth/login/', data=form)
# print('{:*^50}'.format(""))
# print('{:*^50}'.format("Logging in: "))
# print('{:*^50}'.format(""))
# print('Response to login: {}'.format(response.status_code))
# print('Redirecting to: {}'.format(response.url))


response = s.get('http://localhost:8000/sessions/')
print('{:*^50}'.format(""))
print('{:*^50}'.format("Printing all session data"))
print('{:*^50}'.format(""))
pp.pprint(response.json())

session_id = "1"
response = s.get('http://localhost:8000/sessions/'+session_id+ '/')
print('{:*^50}'.format(""))
print('{:*^50}'.format("Printing session id="+session_id))
print('{:*^50}'.format(""))
pp.pprint(response.json())



response = s.get('http://localhost:8000/pipelineconfigurations/')
print('{:*^50}'.format(""))
print('{:*^50}'.format("Printing all PipelineConfiguration data"))
print('{:*^50}'.format(""))
pp.pprint(response.json())

plconf_id = "1"
response = s.get('http://localhost:8000/pipelineconfigurations/'+plconf_id+ '/')
print('{:*^50}'.format(""))
print('{:*^50}'.format("Printing PipelineConfiguration id="+session_id))
print('{:*^50}'.format(""))
pp.pprint(response.json())


response = s.post('http://localhost:8000/observations/', data={"name": "pipodeclouwn", "some_identifier": "1231342352"})
print('{:*^50}'.format(""))
print('{:*^50}'.format("Posting an observation"))
print('{:*^50}'.format(""))
print("Response code: ", response.status_code)
pp.pprint(response.json())

#s.rebuild_auth
print('http://localhost:8000/observations/'+str(response.json()["id"])+'/')
response = s.delete('http://localhost:8000/observations/'+str(response.json()["id"])+'/', data=form)#, data={"id": response.json()["id"]})

s.close()