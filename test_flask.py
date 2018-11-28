
import flask, unittest, flask_testing
from project import views
from project import config

class TestSetup(flask_testing.TestCase):
    def create_app(self): # Works fine
        return views.create_app()

    def test_setup(self): # Works fine
        self.assertTrue(self.app is not None)
        self.assertTrue(self.client is not None)
        self.assertTrue(self._ctx is not None)

class TestViews(flask_testing.TestCase):
    def create_app(self): # Works fine
        return views.create_app()

    def login(self, username, password): # Works fine
        return self.client.post('/login', data=dict(
                user_name=username,
                user_pass=password
        ))   

    def logout(self): # Works fine
        return self.client.get('/logout')

    def test_login(self):
        response = self.login('td', 'password')        
        self.assertEqual(response._status_code, 302)
        self.assertTrue('start' in response.location)

    def test_login_fail(self): # Works fine
        response = self.login('csuder1', 'password2')
        self.assertTrue(b'Invalid password' in response.data)

    def test_logout(self): # Works fine
        response = self.logout()
        self.assertEqual(response._status_code, 302)
        self.assertTrue('login' in response.location)

if __name__ == '__main__':
    unittest.main()