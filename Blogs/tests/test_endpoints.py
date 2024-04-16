from fastapi.testclient import TestClient


def test_add_blog(client:TestClient):
    r = client.post("/blogs/blog", json={"title": "string","description": "string"})
    resposne = r.json()
    assert r.status_code == 200

def test_get_blogs(client:TestClient):
    r = client.get("/blogs/blogs")
    assert r.status_code == 200
    response = r.json()
    assert isinstance(response, list)


def test_get_blog_post_by_id(client:TestClient):
    r = client.get("/blogs/blogs")
    assert r.status_code == 200
    response = r.json()
    blog_id = response[0].get('id')
    r = client.get(f"/blogs/blog/{blog_id}")
    assert r.status_code == 200
    assert isinstance(r.json(), dict)

def test_update_blog_post_by_id(client:TestClient):
    r = client.get("/blogs/blogs")
    assert r.status_code == 200
    response = r.json()
    blog_id = response[0].get('id')
    r = client.put(f"/blogs/blog/{blog_id}", json={"title": "new title","description": "new desription"})
    assert r.status_code == 200

def test_delete_blog_by_id(client:TestClient):
    r = client.get("/blogs/blogs")
    assert r.status_code == 200
    response = r.json()
    blog_id = response[0].get('id')
    r = client.delete(f"/blogs/blog/{blog_id}")
    assert r.status_code == 200