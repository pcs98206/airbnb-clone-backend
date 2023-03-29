from django.db import models
from common.models import CommonModel

# Create your models here.
class Review(CommonModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    experience = models.ForeignKey(
        "experiences.experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}⭐️"
