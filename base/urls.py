from django.urls import path

from . import views
urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logOut, name='logout'),
    path('', views.home, name='home'),
    path('view/<str:pk>/', views.view, name='view'),
    path('create-room/', views.createRoom, name='create-room'),
    path('updated-room/<str:pk>/', views.updatedRoom, name='update-room'),
    path('delete-room/<str:pk>/', views.deleteRoom, name='delete-room'),
    path('register/', views.registerPage, name='register'),
    path('delete-message/<str:pk>/', views.deleteMessage, name='delete-message'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),
]
