
from django.contrib import admin
from django.urls import path, include
# noinspection PyUnresolvedReferences
from trips_app import views as trips_app_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', trips_app_views.index, name='index'),
    path('trip/', include('trips_app.urls')),
    path('account/', include('users_app.urls')),
    path('contact', trips_app_views.contact, name='contact'),
    path('about', trips_app_views.about, name='about'),
    path('map', trips_app_views.map, name='map'),
]

urlpatterns += staticfiles_urlpatterns()
