<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('department',views.department,name='department'),
    path('Details',views.details,name='Details'),
    path('update_message/<str:pk>/',views.updateMessages,name='update_message'),
    path('addFree',views.addFreePeriod,name='addFree'),
    path('addFreeH',views.addFreePeriodH,name='addFreeH'),
    path('schedule',views.schedule,name='schedule'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('take',views.takePeriod,name='take'),
    path('takeH/<str:pk>/',views.takePeriodH,name='takeH'),
    path('add/<str:pk>/',views.addFree,name='add'),
    path('delete',views.delete,name='delete'),
    path('addP/<str:pk>/',views.addP,name='addP'),
    path('deleteH/<str:pk>/',views.deleteH,name='deleteH'),
]
=======
from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('Details',views.details,name='Details'),
    path('update_message/<str:pk>/',views.updateMessages,name='update_message'),
    path('addFree',views.addFreePeriod,name='addFree'),
    path('addFreeH',views.addFreePeriodH,name='addFreeH'),
    path('schedule',views.schedule,name='schedule'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('take',views.takePeriod,name='take'),
    path('takeH/<str:pk>/',views.takePeriodH,name='takeH'),
    path('add/<str:pk>/',views.addFree,name='add'),
    path('delete',views.delete,name='delete'),
    path('addP/<str:pk>/',views.addP,name='addP'),
    path('deleteH/<str:pk>/',views.deleteH,name='deleteH'),
    path('department',views.department,name='department'),
]
>>>>>>> sidhesh
