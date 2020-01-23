from django.db import models

# Create your models here.
class Group_Emotion(models.Model):
    group = models.TextField(default="group")
    emotion = models.TextField(default="emotion")
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Group_Emotion"