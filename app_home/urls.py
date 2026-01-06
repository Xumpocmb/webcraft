from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about_page, name="about_page"),
    path("services/", views.services_page, name="services_page"),
    path("service/<int:pk>/", views.service_detail, name="service_detail"),
    path("why-us/", views.why_us_page, name="why_us_page"),
    path("contact/", views.contact_page, name="contact_page"),
]
