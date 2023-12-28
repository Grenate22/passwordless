from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_verification_email(pin):
    context = {
               "pin":pin
               }
   

    
    html_content = render_to_string("activation.html", context=context)

    email_message = EmailMultiAlternatives()
    email_message.subject = 'Your Account Verification PIN'
    email_message.body = html_content
    email_message.from_email = "noreply@example.com"
    email_message.to = [pin.email]
    email_message.send()



