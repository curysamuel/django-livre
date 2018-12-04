from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from events import models
from django.test import Client
# import json


class EventTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('joe', 'joe@joe.com', 'sam12345')
        self.evento = models.Event.objects.create(name='Rock in Rio', participantes=80000, author=self.user)

    def test_list_view(self):
        self.client.login(username='joe', password='sam12345')
        response = self.client.get(reverse('event_list'))
        self.assertEqual(response.status_code, 200)
        # response = self.client.post(reverse(check_item), json.dumps({}), content_type='application/json')
        