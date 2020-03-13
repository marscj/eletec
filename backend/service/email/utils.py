from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

def render_mail(template_name, subject, from_email, to_email, context):
    
    body = render_to_string(template_name, context)

    msg = EmailMessage(subject, body, from_email, [to_email])
    
    msg.content_subtype = 'html'

    return msg

