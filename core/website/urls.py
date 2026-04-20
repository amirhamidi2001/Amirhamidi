from django.urls import path

from . import views

app_name = "website"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("resume/", views.ResumeView.as_view(), name="resume"),
    path("services/", views.ServicesView.as_view(), name="services"),
    path("portfolio/", views.PortfolioView.as_view(), name="portfolio"),
    path("contact/", views.ContactView.as_view(), name="contact"),
]
