from oscarapi.app import RESTApiApplication

from . import views
from django.conf.urls import include, url
# class MyRESTApiApplication(RESTApiApplication):
# 	def get_urls(self):
# 		urls = super(MyRESTApiApplication, self).get_urls()
# 		return urls

# application = MyRESTApiApplication()


class MyRESTApiApplication(RESTApiApplication):

    def get_urls(self):
        urls = [url(
            r'^profile/',
            views.ProfileView.as_view(), name='api-profile'),
        ]

        return urls + super(MyRESTApiApplication, self).get_urls()


application = MyRESTApiApplication()