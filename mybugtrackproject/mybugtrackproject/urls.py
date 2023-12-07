from django.urls import path
from bugtracker import views
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name='home'),
    path('list_bugs/', views.list_bugs, name='list_bugs'),
    path('add_bug/', views.add_bug, name='add_bug'),
    path('update_bug/<int:pk>/', views.update_bug, name='update_bug'),
    path('delete_bug/<int:pk>/', views.delete_bug, name='delete_bug'),
]
