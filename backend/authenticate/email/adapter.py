
class EmailAdapter(object):

    def __init__(self, request):
        self.request = request

    def render_mail(template_name, subject, from_email, to_email, context):
    
        body = render_to_string(template_name, context)

        msg = EmailMessage(subject, body, from_email, [to_email])
        
        msg.content_subtype = 'html'

        return msg

    def send_mail(self, template_prefix, email, context):
        
