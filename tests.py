import unittest
from main import app
import requests
from datetime import date


class FlaskTestCase(unittest.TestCase):

    # 1 Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    # 2 Ensure that the chatting page loads correctly
    def test_chatting_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Messaging App' in response.data)

    # 3 Ensure response is correct when msg is empty
    def test_none_msg(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(msg='', sender='some', recipient='some'), follow_redirects=True)
        self.assertTrue(b'Message was not sent, Please fill out all required fields', response.data)

    # 3 Ensure response is correct when sender is empty
    def test_none_sender(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(msg='some', sender='', recipient='some'), follow_redirects=True)
        self.assertTrue(b'Message was not sent, Please fill out all required fields', response.data)

    # 4 Ensure response is correct when recipient is empty
    def test_none_recipient(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(msg='some', sender='some', recipient=''), follow_redirects=True)
        self.assertTrue(b'Message was not sent, Please fill out all required fields', response.data)

    # 5 Ensure response is correct when message sent successfully
    def test_msg_sent(self):
        tester = app.test_client(self)
        response = tester.post('/', data=dict(msg='some', sender='some', recipient='some'), follow_redirects=True)
        self.assertTrue(b'Message sent successfully', response.data)






