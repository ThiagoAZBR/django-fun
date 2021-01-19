from django.db import models

class Person(models.Model):
    id = models.AutoField(primary_key = True)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    age = models.IntegerField(default = None, blank = True)
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES, default = None)

class Musician(Person):
    instrument = models.CharField(max_length = 100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    released_date = models.DateField()
    num_stars = models.IntegerField()
