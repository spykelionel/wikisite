from django.test import TestCase
from django.urls import reverse
from datetime import datetime
from django.test import Client
from .models import Bug


class BugModelTests(TestCase):
    def test_bug_creation(self):
        bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date=datetime.strptime("2022-01-01", "%Y-%m-%d").date(),
            status="todo"
        )
        self.assertEqual(bug.description, "Test Bug")
        self.assertEqual(bug.bug_type, "error")
        self.assertEqual(bug.report_date.strftime("%Y-%m-%d"), "2022-01-01")
        self.assertEqual(bug.status, "todo")


class BugViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.bug = Bug.objects.create(
            description="Test Bug",
            bug_type="error",
            report_date="2022-01-01",
            status="todo"
        )

    def test_bug_list_view(self):
        response = self.client.get(reverse('bug_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")

    def test_bug_detail_view(self):
        response = self.client.get(reverse('bug_detail', args=[self.bug.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Bug")
