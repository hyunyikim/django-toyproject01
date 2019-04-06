from django.db import models


class User(models.Model):
    # id 컬럼이 pk로 들어옴
    user_id = models.CharField(max_length=30)
    pwd = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.user_id

class Board(models.Model):
    # id 컬럼이 pk로 들어옴
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    dt = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=2000)
    attached_file = models.CharField(max_length=100)
    hit = models.IntegerField(default=0)

    def __str__(self):
        return self.title