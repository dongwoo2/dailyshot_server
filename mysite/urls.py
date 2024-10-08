"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import erp
from . import settings
from content.views import Main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', Main.as_view()),
    path('content/', include('content.urls')),
    path('shop/', include('shop.urls')),
    path('map/', include('map.urls')),
    path('alcoldrinks/', include('alcoldrinks.urls')),
    path('user/', include('user.urls')),
    path('erp/', include('erp.urls')),
    path('content/', include('content.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#