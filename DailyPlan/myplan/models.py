from django.db import models

class Plan(models.Model):
    TOPIC_CHOICES = [
        ('in_class', '课内学习'),
        ('out_of_class', '课外学习'),
        ('work_task', '工作任务'),
        ('self_improvement', '自我提升'),
    ]

    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    content = models.TextField()
    date = models.DateField()
    flag = models.BooleanField(default=False)  # 0表示未完成，1表示已完成

    def __str__(self):
        return f"{self.topic} - {self.date}"
