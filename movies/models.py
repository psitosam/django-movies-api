from django.db import models

class Movie(models.Model):
  title = models.CharField(max_length=200)
  year = models.IntegerField()

  #override string representation of Movie object when looking at table:
  def __str__(self):
    return f'{self.title} from {self.year}'
    #example: Jaws from 1974