from django.urls import path,include
from .views import user_login,user_signup,user_logout,home_view
urlpatterns = [
    path('',home_view,name='home_view'),
    path('login/',user_login,name='user_login'),
    path('signup/',user_signup,name='user_signup'),
    path('logout/',user_logout,name='user_logout'),
]
