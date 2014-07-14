from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from social.apps import django_app

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auth_test.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/', include(django_app.urls)),
)
