from django.conf.urls import patterns, url

urlpatterns = patterns('gnowsys_ndf.ndf.views.partner',
                       url(r'^/create_partner/', 'create_partner', name='create_partner'),
                       url(r'^/(?P<groups_category>[\w-]+)', 'nroer_groups', name='nroer_groups'),
                   )
