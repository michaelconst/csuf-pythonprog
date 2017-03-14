from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question


class QuestionMethodsTests(TestCase):
    def test_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(question_text="test", pub_date=time)
        self.assertFalse(future_question.was_published_recently(), "future question is not published recently")

    def test_old_question(self):
        old_question = Question(question_text='old test questions', pub_date=timezone.now() - datetime.timedelta(days=10))
        self.assertFalse(old_question.was_published_recently(), 'question from 10 days ago is not recent')

    def test__new_question(self):
        new_question = Question(question_text='new test questions', pub_date=timezone.now() - datetime.timedelta(hours=2))
        self.assertTrue(new_question.was_published_recently(), '2hrs old question is a recent question')
