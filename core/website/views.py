import os

from django.conf import settings
from django.contrib import messages
from django.http import FileResponse, Http404, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class IndexView(TemplateView):
    """View for rendering the main landing page of the website."""

    template_name = "website/index.html"


class AboutView(TemplateView):
    """View for rendering the about page of the website."""

    template_name = "website/about.html"


class ResumeView(TemplateView):
    """View for rendering the resume page of the website."""

    template_name = "website/resume.html"


class ServicesView(TemplateView):
    """View for rendering the services page of the website."""

    template_name = "website/services.html"


class PortfolioView(TemplateView):
    """View for rendering the portfolio page of the website."""

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


class AdsTxtView(View):
    """Serves the ads.txt file from the project's root directory."""

    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, "ads.txt")

        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                content = file.read()
            return HttpResponse(content, content_type="text/plain")
        else:
            raise Http404("ads.txt file not found")


class Custom404View(View):
    """Custom 404 error page view."""

    template_name = "website/404.html"

    def get(self, request, exception=None):
        """Render the custom 404 page."""
        return render(request, self.template_name, status=404)


class DownloadResumeView(View):
    """
    Class-based view to serve a resume PDF file for download.
    Forces download via Content-Disposition header.
    """

    def get(self, request, *args, **kwargs):
        file_path = os.path.join(settings.MEDIA_ROOT, "amir-hamidi.pdf")

        if not os.path.exists(file_path):
            raise Http404("Resume file not found.")

        file_handle = open(file_path, "rb")

        response = FileResponse(file_handle, content_type="application/pdf")

        response["Content-Disposition"] = 'attachment; filename="resume.pdf"'

        return response
