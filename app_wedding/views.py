from django.views.generic.edit import FormView
from .forms import ContactForm
from django.contrib import messages


class ContactFormView(FormView):
    template_name = 'confirmacion.html'
    form_class = ContactForm

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'El mensaje ha sido enviado con éxito! Muchas gracias!')
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return super().form_invalid(form)
