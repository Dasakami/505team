from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return [
            'home', 
            'services',
            'about',
            'fun_list',
            'blog',
            'team',
            

        ]

    def location(self, item):
        return reverse(item)
