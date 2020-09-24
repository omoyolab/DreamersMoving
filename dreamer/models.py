from django.db import models

class Quote(models.Model):
    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    email = models.EmailField(unique=False)
    phone = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    date = models.DateField()
    from_zip = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    to_zip = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    floor = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    square_footage = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    is_elevator = models.BooleanField(default=False)
    amount = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    hear_about_us = models.TextField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.full_name


class Contact(models.Model):
    first_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    email = models.EmailField(unique=False)

    mobile = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )
    body = models.TextField(
        max_length=100,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    


class Review(models.Model):
    stars = models.IntegerField()
    text = models.TextField(max_length=1000, null=False, blank=False)
    author_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)





