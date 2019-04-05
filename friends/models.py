from django.db import models

# Create your models here.


class Friends(models.Model):
    friend1 = models.ForeignKey(
        'friend1',
        on_delete=models.SET_NULL,
        verbose_name="friend 1",
    )
    friend2 = models.ForeignKey(
        'friend2',
        on_delete=models.SET_NULL,
        verbose_name="friend 2",
    )

    @property
    def __str__(self):
        return self.friend1 + " is friends with " + self.friend2

