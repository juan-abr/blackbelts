from django.contrib.sitemaps import Sitemap

from .models import BlackBelt

class BlackBeltSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlackBelt.objects.all()

    # def lastmod(self, obj):
    #     return obj.updated