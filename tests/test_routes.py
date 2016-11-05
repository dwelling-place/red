import json

def test_list(client):
    assert client.get('/projects').status_code == 200

def test_crud(client):
    resp = client.post('/projects', data={'name': 'spam'})
    assert resp.status_code == 201
    loc = resp.headers['Location']
    assert loc
    print(loc)

    resp = client.get(loc)
    assert resp.status_code == 200
    print(resp.json)
    assert resp.json['name'] == 'spam'

    assert client.put(loc, data={'name': 'eggs'}).status_code in (200, 202, 204)

    resp = client.get(loc)
    assert resp.status_code == 200
    assert resp.json['name'] == 'eggs'

    assert client.delete(loc).status_code in (200, 202, 204)
