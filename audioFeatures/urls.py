from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'af_documentation.views.home', name='home'),
     url(r'^processor/samples/', 'audio_processor.views.getSamples', name='audio_processor_samples'),
     url(r'^processor/$', 'audio_processor.views.process', name='audio_processor'),
     url(r'^process_chain/', 'audio_processor.views.process_chain', name='process_chain'),

     url(r'^inplaceeditform/', include('inplaceeditform.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
