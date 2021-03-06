from django.db import models
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from multiselectfield import MultiSelectField


MY_CHOICES = (('english', 'English Language'),
              ('math', 'Mathematics'),
              ('geography', 'Geography'),
              ('chemistry', 'Chemistry'),
              ('physics', 'Physics'))


class Exams(models.Model):
    name = models.CharField(max_length=64, verbose_name=u'Exam Body Name')
    logoUrl = models.ImageField(upload_to='staff', verbose_name=u'Exam Body Logo', blank=True)
    subjects = MultiSelectField(choices=MY_CHOICES)
    startDate = models.IntegerField(verbose_name=u'Start of Exam Years', blank=True)
    stopDate = models.IntegerField(verbose_name=u'End of Exam Years', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        ordering = ['name', 'subjects', 'startDate', 'stopDate']


class ExamSubject(models.Model):
    exam = models.CharField(max_length=64, verbose_name=u'Exam name')
    slug = models.SlugField(unique=True)
    subject = models.CharField(max_length=64, verbose_name=u'Subject name', null=True, blank=True)
    year = models.IntegerField(verbose_name=u'Exam Year', blank=True)
    duration = models.IntegerField(verbose_name=u'Subject Duration', null=True, blank=True)

    def __str__(self):
        return "{exam} - {subject} - {year} - {duration}".format(exam=self.exam, subject=self.subject,
                                                                 year=self.year, duration=self.duration)

    class Meta:
        verbose_name = "ExamSubject"
        verbose_name_plural = "ExamSubjects"
        ordering = ['exam', 'subject', 'year']


# each questions with relationship to an exam, year and subject
class Question(models.Model):
    question_text = models.TextField(verbose_name=u'Question\'s text')
    serial_no = models.IntegerField(verbose_name='Question\'s index',
                                    help_text='Questions will be shown based on their index')
    is_published = models.BooleanField(default=False)
    exam = models.ForeignKey(ExamSubject, related_name='questions', on_delete=models.CASCADE)
    correct = models.TextField(verbose_name=u'Correct Answer\'s text', blank=True)

    def __str__(self):
        return "{index} - {exam}".format(index=self.serial_no, exam=self.exam)

    class Meta:
        verbose_name = "Question"
        verbose_name_plural = "Questions"
        ordering = ['serial_no']


# answers to a question
class Answer(models.Model):
    text = models.TextField(verbose_name=u'Answer\'s text')
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Answer"
        verbose_name_plural = "Answers"


# details of each instance of an exam taken by a user and his response with score
class UserScore(models.Model):
    user = models.ForeignKey(User, related_name='myscores', on_delete=models.CASCADE)
    exam = models.ForeignKey(ExamSubject, related_name='myscoresexam')
    score = models.CharField(max_length=20, verbose_name='my score')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{username} - {exam} - {score}".format(username=self.user.username, exam=self.exam, score=self.score)

    class Meta:
        verbose_name = "UserScore"
        verbose_name_plural = "UserScores"
        ordering = ['created_on']
