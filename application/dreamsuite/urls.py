from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from django.contrib.auth import views as auth_views
from dataentry import views as dataentry_views
from static_border_stations import views as static_border_stations_views


admin.autodiscover()

urlpatterns = [
    url(r'^$', dataentry_views.home, name='home'),
    url(r'^data-entry/', include('dataentry.urls')),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^events/', include('events.urls')),

    url(r'^api/', include('accounts.urls')),
    url(r'^api/', include('budget.urls')),
    url(r'^api/', include('rest_api.urls')),
    url(r'^api/', include('portal.urls')),
    url(r'^api/', include('static_border_stations.urls')),

    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout_then_login, name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),

    # Support old style base36 password reset links; remove in Django 1.7
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^interceptee_fuzzy_matching/', dataentry_views.interceptee_fuzzy_matching, name='interceptee_fuzzy_matching'),
    url(r'^get_station_id/', static_border_stations_views.get_station_id, name='get_station_id')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
