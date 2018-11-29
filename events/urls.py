from django.urls import path

from events import views

urlpatterns = [
    path('', views.EventList.as_view(), name='event_list'),
    path('view/<int:pk>', views.EventView.as_view(), name='event_view'),
    path('new', views.EventCreate.as_view(), name='event_new'),
    path('view/<int:pk>', views.EventView.as_view(), name='event_view'),
    path('edit/<int:pk>', views.EventUpdate.as_view(), name='event_edit'),
    path('delete/<int:pk>', views.EventDelete.as_view(), name='event_delete'),
]
