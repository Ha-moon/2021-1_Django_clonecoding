import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self): #미래
        """
        was_published_recently() returns False를 반환한다 for questions whose pub_date가 미래일때,
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30) #  pub_date필드가 30일 이후(미래)인
        future_question = Question(pub_date=time) # Question 인스턴스를 생성
        self.assertIs(future_question.was_published_recently(), False) # pub_date가 미래에 있다면 False를 반환해야함.


    def test_was_published_recently_with_old_question(self): # 과거
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=time)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self): #최근
        """
        was_published_recently() returns True for questions whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time)
        self.assertIs(recent_question.was_published_recently(), True)