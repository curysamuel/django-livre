"""my_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView
from django.urls import include
from events import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', TemplateView.as_view(template_name='logout.html'), name='logout'),
    path('new', views.EventCreate.as_view(), name='event_new'),
    path('view/<int:pk>', views.EventView.as_view(), name='event_view'),
    path('edit/<int:pk>', views.EventUpdate.as_view(), name='event_edit'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='event_delete'),
    path('', views.EventList.as_view(), name='event_list'),
]
