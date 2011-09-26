from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.contrib import databrowse

admin.autodiscover()

urlpatterns = patterns('',
                       # base test
                       url(r'^$', direct_to_template, {'template': 'base.html'}),
                       url(r'^items/', include('brownie.items.urls')),
                       # Examples:
                       # url(r'^$', 'pathfinder.views.home', name='home'),
                       # url(r'^pathfinder/', include('pathfinder.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
                       url(r'^grappelli/', include('grappelli.urls')),
                       )
