from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Service

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'about_page', 'services_page', 'why_us_page', 'contact_page']

    def location(self, item):
        return reverse(item)

class ServiceSitemap(Sitemap):
    def items(self):
        return Service.objects.all()
