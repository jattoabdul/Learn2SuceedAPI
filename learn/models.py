from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Exam name')
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        ordering = ['name']


class Subject(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Subject name', null=True, blank=True)
    # duration = models.IntegerField(verbose_name=u'Subject Duration', null=True, blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subject"
        verbose_name_plural = "Subjects"
        ordering = ['name']


# years for exams
class Year(models.Model):
    year_number = models.IntegerField(verbose_name=u'Exam Year', blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name = "Year"
        verbose_name_plural = "Years"
        ordering = ['year_number']


# each questions with relationship to an exam, year and subject
class Question(models.Model):
    question_text = models.CharField(max_length=30000, verbose_name=u'Question\'s text')
    serial_no = models.IntegerField(unique=True, verbose_name='Question\'s index',
                                    help_text='Questions will be shown based on their index, ' +
                                              'and this index is shown as the question number')
    is_published = models.BooleanField(default=False)
    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    year = models.ForeignKey(Year, related_name='questions', verbose_name='Question Exam\'s year',
                             on_delete=models.CASCADE)

    def __str__(self):
        return "{index} - {content} - {subject}".format(index=self.serial_no, content=self.question_text, subject=self.subject)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['serial_no']


# answers to a question
class Answer(models.Model):
    text = models.CharField(max_length=128, verbose_name=u'Answer\'s text')
    is_valid = models.BooleanField(default=False, help_text='tick if answer is correct choice')
    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


# details of each instance of an exam taken by a user and his response with score
class UserScore(models.Model):
    user = models.ForeignKey(User, related_name='myscores', on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, related_name='myscores')
    subject = models.ForeignKey(Subject, related_name='myscores')
    score = models.CharField(max_length=20, verbose_name='my score')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{username} - {subject} - {score}".format(username=self.user.username, subject=self.subject,
                                                         score=self.score)

    class Meta:
        verbose_name = "UserScore"
        verbose_name_plural = "UserScores"
        ordering = ['created_on']


# leadersboard table with username and the total score of all exam instance taken
class LeadersBoard(models.Model):
    user_exam = models.ForeignKey(UserScore, related_name='leadersboard', on_delete=models.CASCADE)
    points = models.CharField(max_length=20, verbose_name='total points')  # total scores of UserScores for each user

    def __str__(self):
        return "{username} - {points}".format(username=self.user_exam, points=self.points)

    class Meta:
        verbose_name = "LeaderBoard"
        verbose_name_plural = "LeadersBoard"
        ordering = ['points']