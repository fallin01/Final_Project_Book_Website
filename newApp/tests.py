"""from _typeshed import Self
import datetime
from django.http import response
from django.test import TestCase
from django.utils import timezone

import newApp
from .models import Question
from django.urls import reverse
# Create your tests here.

class QuestionModelTest(TestCase):
    def test_was_published_recently_with_future_question(self):
        time = timezone.now() + datetime.timedelta(days=30)
        futureQuestion = Question(pubDate= time)
        self.assertIs(futureQuestion.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        oldQuestion = Question(pubDate=time)
        self.assertIs(oldQuestion.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recentQuestion = Question(pubDate=time)
        self.assertIs(recentQuestion.was_published_recently(), True)

def create_question(questionText, days):
        time = timezone.now() + datetime.timedelta(days=days)
        return Question.objects.create(questionText=questionText, pubDate=time)

class QuestionIndexViewsTests(TestCase):
    def test_no_question(self):
        response = self.client.get(reverse('newApp:index'))
        self.assertQuerysetEqual(response.status_code, 200)
        self.assertContains(response, "No posts")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])    

    def test_past_question(self):
        question = create_question(questionText="Past question", days=-30)
        response = self.client.get(reverse('newApp:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [question], )

    def testFutureQuestion(self):
        create_question(questionText="Future question", days=30)
        response = self """