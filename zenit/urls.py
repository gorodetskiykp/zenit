"""zenit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^systems/', include('isystems.urls')),
    url(r'^organizations/', include('organizations.urls')),
    url(r'^people/', include('people.urls')),
    url(r'^contracts/', include('contracts.urls')),
    url(r'^planpost/', include('planpost.urls')),
    url(r'^schedules/', include('schedule_charts.urls')),
    url(r'^docs/', include('docs.urls')),
    url(r'^help/', include('help_info.urls')),
    url(r'^admin/', admin.site.urls),

    url(r'^$', TemplateView.as_view(template_name = 'index.html')),
]

if settings.PRODUCTION is False:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
