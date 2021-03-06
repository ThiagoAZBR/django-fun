from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def chamar(self):
        print(f'{self.first_name} {self.last_name}')

class Publication(models.Model):
    title = models.CharField(max_length = 30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Article(models.Model):
    headline = models.CharField(max_length = 100)
    pub_date = models.DateTimeField()
    reporter = models.ForeignKey(Reporter, on_delete = models.CASCADE)
    publications = models.ManyToManyField(Publication)

    def __str__(self):
        return self.headline

class Meta:
    ordering = ['headline']