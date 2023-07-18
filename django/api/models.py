import os
import stripe
import uuid
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from pygments import highlight
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)
    stripe_id = models.CharField(max_length=100, blank=True)

# @receiver(post_save, sender=User )
# def create_account(sender, instance, created, **kwargs):
#     if created:
#         print(instance)
#         # account = Account.create(user=instance.user)


class Domain(models.Model):
    user = models.ForeignKey(User, related_name='domains', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    last_scan = models.TextField(blank=True, null=True)
    scan_status = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Scan(models.Model):
    user = models.ForeignKey(User, related_name='scans', on_delete=models.CASCADE)
    domain = models.ForeignKey(Domain, related_name='scans', on_delete=models.CASCADE)
    name = models.UUIDField(default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    last_scan = models.TextField()
    
    def __str__(self):
        return self.name


LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Snippet(models.Model):
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ['created']

    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)


class StripeCustomer(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    customer_id = models.CharField(max_length=255)
    subscription_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.pk}-{self.user.username}"


@receiver(post_save, sender=User)
def create_stripe_customer(sender, instance, created, **kwargs):
    if created == True:
        stripe.api_key = os.environ.get('STRIPE_SECRET_KEY', 'django needs a stripe secret key')
        cust = stripe.Customer.create(description=f"{instance.pk}-{instance.username}",)
        StripeCustomer.objects.create(user=instance, customer_id=cust.id)


class StripeProduct(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)
    product_id = models.CharField(max_length=255)
    amount = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return self.name