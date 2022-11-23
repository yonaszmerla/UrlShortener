from django.test import TestCase

# Create your tests here.


class TestApi(TestCase):

    def test_index(self):
        response = self.client.get('http://localhost:8000/')
        assert response.status_code == 200

    def test_create(self):
        response = self.client.post('http://localhost:8000/create', data={'url': 'https://www.google.com'})
        assert response.status_code == 200
        assert response.content.decode('utf-8').startswith('http://localhost:8000/short/')

    def test_create_no_url(self):
        response = self.client.post('http://localhost:8000/create', data={})
        assert response.status_code == 400

    def test_short(self):
        response = self.client.post('http://localhost:8000/create', data={'url': 'https://www.google.com'})
        assert response.status_code == 200
        assert response.content.decode('utf-8').startswith('http://localhost:8000/short/')
        short_url = response.content.decode('utf-8')
        response = self.client.get(short_url)
        assert response.status_code == 302
        assert response.url == 'https://www.google.com'

    def test_short_not_found(self):
        response = self.client.get('http://localhost:8000/short/1')
        assert response.status_code == 404



