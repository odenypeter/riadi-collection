from django.db import models


class MainSliderData(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    image = models.ImageField(
        upload_to='uploads',
        help_text='Image Size should be 484x441'
    )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class PolicyTerm(models.Model):
    terms_of_use = models.TextField(null=True, blank=True)
    privacy_policy = models.TextField(null=True, blank=True)
    refund_policy = models.TextField(null=True, blank=True)
    billing_system = models.TextField(null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.create_date}'


class PublicMessage(models.Model):
    subject = models.CharField(max_length=150)
    sender_email = models.CharField(max_length=150)
    message = models.TextField()
    received_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.subject


class Currency(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=8, null=True, blank=True)
    symbol = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class GeneralInfo(models.Model):
    email_address = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    facebook_link = models.TextField(null=True, blank=True)
    twitter_link = models.TextField(null=True, blank=True)
    linkedin_link = models.TextField(null=True, blank=True)
    instagram_link = models.TextField(null=True, blank=True)
    street_name = models.CharField(max_length=150, null=True, blank=True)
    zip_code = models.CharField(max_length=150, null=True, blank=True)
    city = models.CharField(max_length=150, null=True, blank=True)
    currency = models.ForeignKey(Currency, null=True, on_delete=models.SET_NULL)
    active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.email_address}' or 'core'

