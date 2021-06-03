from django.db import models

PREFIX_CHOICES = (
    ('Kwan Jang Nim', 'kjn'),
    ('Sa Bum Nim', 'sbn'),
    ('Kyo Sa Nim', 'ksn'),
    ('Mr.', 'mr'),
    ('Ms.', 'ms'),
    ('', '')
)

# Create your models here.
class BlackBelt (models.Model):
    prefix          = models.CharField(
        choices = PREFIX_CHOICES,
        default = '',
        max_length = 20)
    first_name      = models.CharField(max_length = 20)
    last_name       = models.CharField(max_length = 20)
    birthday        = models.DateField(blank=True)
    rank            = models.CharField(max_length = 20)
    rank_received   = models.DateField(blank=True)
    instructor_bio  = models.TextField(blank = True)
    image_url       = models.CharField(max_length = 20, blank = True)

    class Meta:
        ordering = ['prefix', 'rank', 'birthday', 'rank_received', 'last_name']

    def __str__(self):
        return self.first_name + " " + self.last_name