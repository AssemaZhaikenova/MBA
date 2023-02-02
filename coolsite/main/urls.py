from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-index'),
    path('about/', views.about, name='main-about'),
    path('login/', views.login_v, name='main-login'),
    path('lesson/', views.lesson, name='main-lesson'),
    path('mylessons/', views.mylesson, name='main-mylessons'),
    path('logout/', views.logout_view, name='main-logout'),
    path('requests/', views.requests, name='main-requests'),
    path('addrequest/', views.select_view, name='main-addrequest'),
    path('coach/', views.coach, name='main-coach'),
    path('disciplines/', views.disciplines, name='main-disciplines'),

]