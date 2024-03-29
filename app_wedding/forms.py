from django import forms
from django.core.mail import get_connection, send_mail
from django.conf import settings


class ContactForm(forms.Form):

    name = forms.CharField(error_messages={'required': 'Por favor, indique su nombre'})
    bus = forms.CharField(error_messages={'required': 'Por favor, indique indique si acudirá en autobús'})
    guests = forms.CharField(error_messages={'required': 'Por favor, indique el número total de invitados'})
    message = forms.Textarea()

    def send_email(self):
        with get_connection(
                host=settings.EMAIL_HOST,
                port=settings.EMAIL_PORT,
                username=settings.EMAIL_FEEDBACK_USER,
                password=settings.EMAIL_FEEDBACK_PASSWORD,
                use_tls=settings.EMAIL_USE_TLS
        ) as connection:
            send_mail(
                f"Confirmación de asistencia: {self.data['name']}",
                f"Número de invitados: {self.data['guests']}\nAutobús?: {self.data['bus']}\nAlgún mensaje especial: {self.data['message']}",
                settings.EMAIL_FEEDBACK_USER,
                settings.EMAIL_RECIPIENT_LIST,
                connection=connection,
                fail_silently=False,
            )
