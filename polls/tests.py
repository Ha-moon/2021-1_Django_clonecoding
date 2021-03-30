import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question


class QuestionModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False를 반환한다 for questions whose pub_date가 미래일때,
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30) #  pub_date필드가 30일 이후(미래)인
        future_question = Question(pub_date=time) # Question 인스턴스를 생성
        self.assertIs(future_question.was_published_recently(), False)