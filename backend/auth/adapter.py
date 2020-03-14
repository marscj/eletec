from django.template.loader import render_to_string
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings

class AuthAdapter(object):

    def __init__(self, request):
        self.request = request

    def render_mail(self, template_name, subject, to_email, context):
    
        body = render_to_string(template_name, context)

        from_email = settings.DEFAULT_FROM_EMAIL

        msg = EmailMessage(subject, body, from_email, [to_email])
        
        msg.content_subtype = 'html'

        return msg

    def send_mail(self, template_name, subject, email, context):
        msg = self.render_mail(template_name, subject, email, context)
        msg.send()

    def render_sms(self, template_name, )

        from_phone = settings.SENDSMS_FROM_NUMBER

        return SmsMessage(
            body='[Eletec] Your verification code is %s' % otp,
            from_phone=from_phone,
            to=phone_number
        )