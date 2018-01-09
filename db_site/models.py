from django.db import models
from django.utils import timezone

# Create your models here.
class Studio(models.Model):
    name = models.CharField(max_length=200)
    twitter = models.CharField(max_length=200, blank=True, default='')
    facebook = models.CharField(max_length=200, blank=True, default='')
    instagram = models.CharField(max_length=200, blank=True, default='')
    youtube = models.CharField(max_length=200, blank=True, default='')
    url = models.CharField(max_length=255)
    country = models.CharField(max_length=200)
    region = models.CharField(max_length=200, blank=True, default='')
    language = models.CharField(max_length=200)
    ship_international = models.BooleanField()
    currency = models.CharField(max_length=20)
    price_max = models.PositiveIntegerField()
    price_min = models.PositiveIntegerField()
    avg_wait = models.CharField(max_length=200)
    notes = models.TextField(blank=True, default='')
    is_active_comment = models.CharField(max_length=3, choices=[('ACT', 'Active'), ('HIA','Hiatus'), ('CLO','Closed')], default='ACT')
    date_added = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    added_by = models.ForeignKey('auth.User', on_delete = models.CASCADE, related_name='%(class)s_studio_created')
    approved_by = models.ForeignKey('auth.User', null=True, blank=True, on_delete= models.CASCADE)

    def approve(self, request):
        self.is_approved = True
        self.approved_by = request.user
        self.publish()

    def publish(self):
        self.last_updated = timezone.now()

    def __str__(self):
        return self.name
