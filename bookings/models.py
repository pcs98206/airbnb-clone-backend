from django.db import models
from common.models import CommonModel

# Create your models here.
class Booking(CommonModel):
    class BookingKindChoices(models.TextChoices):
        ROOM = "room", "ROOM"
        EXPERIENCE = "experience", "EXPERIENCE"

    kind = models.CharField(
        max_length=50,
        choices=BookingKindChoices.choices,
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    check_in = models.DateField(
        blank=True,
        null=True,
    )
    check_out = models.DateField(
        blank=True,
        null=True,
    )
    experience_time = models.DateTimeField(
        blank=True,
        null=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for : {self.user}"
