from django.db    import models
from users.models import User


class Todo(models.Model):
    title       = models.CharField(max_length=200 , null=True)
    description = models.TextField()
    user = models.ForeignKey("users.User" , on_delete=models.CASCADE)

    class Meta:
        db_table="todos"

