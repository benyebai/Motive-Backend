from django.contrib.auth.models import User
from django.db import models

class Friendship(models.Model):
    # this is a 2 way model
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendship_user2')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (('user1', 'user2'),)

    def save(self, *args, **kwargs):
        # Always store in consistent order to enforce uniqueness
        if self.user1.id > self.user2.id:
            self.user1, self.user2 = self.user2, self.user1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user1.username} ↔ {self.user2.username}"
    
class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='sent_requests', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='received_requests', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        unique_together = ('from_user', 'to_user')

    def __str__(self):
        return f"{self.from_user.username} → {self.to_user.username} (Accepted: {self.accepted})"

class HangoutEvent(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    attendee_count = models.IntegerField()
    date_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} by {self.created_by.username}"

