from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    questionnaire_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
     Profile.objects.create(user=instance)

class QuestionnaireResponse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    school_language = models.CharField(max_length=50)
    stage_activity = models.CharField(max_length=50)

    extempore_comfort = models.IntegerField()
    public_speaking_confidence = models.IntegerField()
    help_seeking_comfort = models.IntegerField()
    group_discussion_confidence = models.IntegerField()
    adaptability = models.IntegerField()

    total_score = models.IntegerField(default=0)

    def calculate_score(self):

     language_score = {
        "english": 3,
        "hindi": 2,
        "regional": 1
     } .get(self.school_language, 1)

     stage_score = {
        "very_much": 3,
        "rarely": 2,
        "never": 1
     }.get(self.stage_activity, 1)

     pressure_score = {
        "motivated": 3,
        "anxious": 2,
        "overwhelmed": 1
     }.get(self.academic_pressure, 1)

     self.total_score = (
        language_score +
        stage_score +
        pressure_score +
        self.extempore_comfort +
        self.public_speaking_confidence +
        self.help_seeking_comfort +
        self.group_discussion_confidence +
        self.adaptability
    )

     self.save()
