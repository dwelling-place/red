
def test_get_projects(client):
	assert client.get('/projects').status_code == 200

def test_project(client):
	resp = client.post('/projects', data={'name': 'spam'})
	assert resp.status_code == 201
	loc = resp.headers['Location']
	assert loc
	print(loc)

	assert client.get(loc).status_code == 200

	assert client.put(loc, data={'name': 'eggs'}).status_code in (200, 202, 204)

	assert client.delete(loc).status_code in (200, 202, 204)
