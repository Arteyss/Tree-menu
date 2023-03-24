from django.urls import path

from .views import view_index

urlpatterns = [
    path('', view_index,),
    path('about', view_index, name='about'),
    path('auth', view_index, name='auth'),
    path('auth/login', view_index, name='login'),
    path('auth/registrations', view_index, name='registrations'),
    path('start_page', view_index, name='start_page'),
]
