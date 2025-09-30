from django.test import TestCase
from .models import TeamMember
import sys

class TestTeam(TestCase):

    def test_index(self):
        response = self.client.get('/team/')
        self.assertEqual(response.status_code, 200)

    def test_timur(self):
        res = self.client.get('/team/timur')
        self.assertEqual(res.status_code, 301)

    def test_timur_content(self):
        res = self.client.get('/team/timur')
        with open('test_response.html', 'w', encoding='utf-8') as f:
            f.write(res.content.decode())
        self.assertEqual(res.status_code, 301)



