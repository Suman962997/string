from django.db import models


class Level(models.Model):
    id = models.AutoField(primary_key=True)
    level_name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True) 

    class Meta:
        managed = False
        db_table = 'hierarchy\".\"Level'

    def __str__(self):
    	return self.level_name

 