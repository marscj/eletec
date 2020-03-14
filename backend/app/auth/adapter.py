from django.template.loader import render_to_string
from django.template import TemplateDoesNotExist
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.conf import settings

from core.sms import SmsMessage

class AuthAdapter(object):

    def __init__(self, request):
        self.request = request

    def render_mail(self, template_prefix, subject, to_email, context):

        # body = render_to_string(template_name, context)

        # msg = EmailMessage(subject, body, from_email, [to_email])
        
        # msg.content_subtype = 'html'

        # return msg

        subject = render_to_string('{0}_subject.txt'.format(template_prefix), context)
        subject = ' '.join(subject.splitlines()).strip()

        from_email = settings.DEFAULT_FROM_EMAIL

        bodies = {}
        for ext in ['html', 'txt']:
            try:
                template_name = '{0}_message.{1}'.format(template_prefix, ext)
                bodies[ext] = render_to_string(template_name,
                                               context).strip()
            except TemplateDoesNotExist:
                if ext == 'txt' and not bodies:
                    # We need at least one body
                    raise
        if 'txt' in bodies:
            msg = EmailMultiAlternatives(subject,
                                         bodies['txt'],
                                         from_email,
                                         [to_email])
            if 'html' in bodies:
                msg.attach_alternative(bodies['html'], 'text/html')
        else:
            msg = EmailMessage(subject,
                               bodies['html'],
                               from_email,
                               [to_email])
            msg.content_subtype = 'html'  # Main content is now text/html
        return msg

    def render_sms(self, template_name, to_number, context)

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

    def send_sms(self, template_name, to_number, context)
        msg = render_sms(template_name, to_number, context)

    def send_confirmation_mail(self, request, emailconfirmation):
        activate_url = request.build_absolute_uri('/auth/confirmation_mail?key=' + emailconfirmation.key)
        
        ctx = {'activate_url': activate_url}

        email_template = 'email_confirmation'

        self.send_mail(email_template, emailconfirmation.email_address.email, ctx)

    def send_confirmation_sms(self, request, phoneconfirmation):

        email_template = 'phone_confirmation_message.txt'

        ctx = {'otp': phoneconfirmation.otp}

        self.send_sms(email_template, phoneconfirmation.phone_number, ctx)

