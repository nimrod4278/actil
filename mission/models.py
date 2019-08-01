from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.urls import reverse


MISSION_STATUS_CHOICES = [
    ('A', 'Active'),
    ('D', 'Deactivated'),
]


class MissionQuerySet(models.QuerySet):
    def count_user_active_missions(self, user):
        return self.filter(
            Q(status='A') & Q(owner=user)
        ).count()

    def user_active_missions(self, user):
        return self.filter(
            Q(status='A') & Q(owner=user)
        )


class Mission(models.Model):
    name = models.CharField(max_length=300, blank=False, default='0', primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mission_owner")
    start_time = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, default='A', choices=MISSION_STATUS_CHOICES)

    objects = MissionQuerySet.as_manager()

    def get_absolute_url(self):
        """
         defines what a utl to retrun by id of a game
        :return:
        """
        return reverse('mission_detail', args=[self.id])

    def __str__(self):
        return "{0} by {1}".format(self.name, self.owner)


class Keyword(models.Model):
    word = models.CharField(max_length=100, blank=False, primary_key=True)
    missions = models.ManyToManyField(Mission, related_name="keyword_missions")

    def __str__(self):
        return self.word
