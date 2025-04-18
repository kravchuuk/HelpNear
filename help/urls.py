from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_request, name='create_request'),
    path('request/<int:request_id>/', views.request_detail, name='request_detail'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('my-requests/', views.my_requests, name='my_requests'),
path('request/<int:request_id>/accept/<int:response_id>/', views.accept_response, name='accept_response'),
path('rate/<int:response_id>/', views.rate_helper, name='rate_helper'),
    

]
