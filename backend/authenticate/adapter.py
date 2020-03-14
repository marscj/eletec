from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings

from core.sms.message import SmsMessage

class AuthAdapter(object):

    def __init__(self, request):
        self.request = request

    def render_mail(self, template_prefix, subject, to_email, context):

        from_email = settings.DEFAULT_FROM_EMAIL
        subject = render_to_string('{0}_subject.txt'.format(template_prefix))
        body = render_to_string('{0}_message.html'.format(template_prefix, ext), context)

        msg = EmailMessage(subject, body, from_email, [to_email])
        msg.content_subtype = 'html'
        return msg

    def render_sms(self, template_name, to_number, context):

        from_phone = settings.SENDSMS_FROM_NUMBER

        body = render_to_string(template_name, context)

        return SmsMessage(
            body=body,
            from_phone=from_phone,
            to=to_number
        )

    def send_mail(self, template_prefix, subject, to_email, context):
        msg = self.render_mail(template_prefix, subject, to_email, context)
        msg.send()

    def send_sms(self, template_name, to_number, context):
        msg = render_sms(template_name, to_number, context)

    def send_confirmation_mail(self, emailconfirmation):
        activate_url = self.request.build_absolute_uri('/auth/confirmation_mail?key=' + emailconfirmation.key)
        
        ctx = {'activate_url': activate_url}

        email_template = 'email_confirmation'

        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)

    def send_confirmation_sms(self, phoneconfirmation):

        email_template = 'phone_confirmation_message.txt'

        ctx = {'otp': phoneconfirmation.otp}

        self.send_sms(email_template, phoneconfirmation.phone_number, ctx)

