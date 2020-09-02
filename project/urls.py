from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('Auction/',include('auction.urls')),
    path('Auction/', include('django.contrib.auth.urls')),
    path('health', lambda request : HttpResponse('okay')),
]



if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
