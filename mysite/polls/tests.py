# Create your tests here.
import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=2)
        print("Hello")
        print(time)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)