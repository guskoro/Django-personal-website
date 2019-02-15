from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('about/', include('about.urls')),
    path('blog/', include('blog.urls')),
    path('cv/', include('cv.urls')),
    path('contact/', include('contact.urls')),
    path('story/', include('about.urls')),
]
