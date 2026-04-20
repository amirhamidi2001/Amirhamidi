from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class IndexView(TemplateView):
    """
    View for rendering the main landing page of the website.
    """

    template_name = "website/index.html"


class AboutView(TemplateView):
    """
    View for rendering the about page of the website.
    """

    template_name = "website/about.html"


class ResumeView(TemplateView):
    """
    View for rendering the resume page of the website.
    """

    template_name = "website/resume.html"


class ServicesView(TemplateView):
    """
    View for rendering the services page of the website.
    """

    template_name = "website/services.html"


class PortfolioView(TemplateView):
    """
    View for rendering the portfolio page of the website.
    """

    template_name = "website/portfolio.html"


class ContactView(FormView):
    """
    Handles display and processing of the contact form.
    """

    template_name = "website/contact.html"
    form_class = ContactForm
    success_url = reverse_lazy("website:contact")

    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent. Thank you!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error with your submission.")
        return super().form_invalid(form)