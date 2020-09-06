from django.urls import path
from django.conf.urls import url
from users import views 

urlpatterns = [
    path('user_details', views.user_details, name='user_details')
    
]
