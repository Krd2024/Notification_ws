from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Notification(models.Model):
    NOTIFICATION_TYPES = (
        ("like", "Like"),
        ("answer", "Answer"),
        ("signal", "Signal"),
    )

    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications_sent"
    )  # от кого

    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notifications_received"
    )  # кому
    notification_type = models.CharField(max_length=10, choices=NOTIFICATION_TYPES)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    related_object_id = models.PositiveIntegerField()

    class Meta:
        ordering = ["-created_at"]

        # unique_together = (
        #     "notification_type",
        #     "related_object_id",
        #     "sender",
        #     "recipient",
        # )

    def __str__(self):
        return f"{self.get_notification_type_display()} для {self.recipient.username}"


# Create your models here.
