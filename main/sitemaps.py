from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = "daily"

    def items(self):
        return [
            'home', 
            'service_detail',
            'services',
            'about',
            'fun_list',
            'blog_detail',
            'blog',
            'team',
            'member_detail',
            'portfolio_detail',
            
        ]

    def location(self, item):
        return reverse(item)
