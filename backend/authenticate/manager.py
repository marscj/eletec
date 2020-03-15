from django.db import models

class EmailAddressManager(models.Manager):

    def add_email(self, request, email, user):
                  
        email_address, created = self.get_or_create(email=email, user=user)

        if created:
            email_address.send_confirmation(request)

        return email_address