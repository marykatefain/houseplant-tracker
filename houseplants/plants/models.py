from django.db import models


class Species(models.Model):
    scientific_name = models.CharField(max_length=200, blank=True, null=True)
    common_name = models.CharField(max_length=200, blank=True, null=True)
    LIGHT_REQUIREMENT_CHOICES = (
        ('DIRECT', 'Direct Bright'),
        ('INDIRECT', 'Indirect Bright'),
        ('MEDIUM', 'Medium'),
        ('LOW', 'Low'),
    )
    light_requirement = models.CharField(
        max_length=200,
        choices=LIGHT_REQUIREMENT_CHOICES,
        default='INDIRECT',
    )
    TEMP_REQUIREMENT_CHOICES = (
        ('MEDIUM', '60 - 80 deg F'),
    )
    temp_requirement = models.CharField(
        max_length=200,
        choices=TEMP_REQUIREMENT_CHOICES,
        default='MEDIUM',
    )
    HUMIDITY_REQUIREMENT_CHOICES = (
        ('HIGH', 'High Humidity'),
        ('MEDIUM', 'Medium Humidity'),
        ('LOW', 'Low Humidity'),
    )
    humidity_requirement = models.CharField(
        max_length=200,
        choices=HUMIDITY_REQUIREMENT_CHOICES,
        default='MEDIUM',
    )

    def __str__(self):
        return self.common_name


class Plant(models.Model):
    nick_name = models.CharField(max_length=200, blank=True, null=True)
    species = models.ForeignKey(
        Species,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    adoption_date = models.DateTimeField('adoption date', blank=True, null=True)
    profile_pic = models.ImageField(blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.nick_name
