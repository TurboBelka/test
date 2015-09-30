from django.db import models


# Create your models here.
class AuthorTest(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.first_name + self.last_name


class ArticleTest(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(AuthorTest)
