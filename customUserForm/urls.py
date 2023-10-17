from django.urls import path
from customUserForm import views

urlpatterns = [
   path('',views.sign_up,name='CustUserForm'),
   path("userlogin",views.user_login,name='user_login'),
   path("UserProfile",views.user_profile,name='profile'),
   path("UserLogout",views.user_logout,name='logout')

]