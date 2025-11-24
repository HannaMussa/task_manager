from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.task_list, name='task-list'),
    path('task/<int:pk>/edit/', views.task_edit, name='task-edit'),
    path('task/<int:pk>/delete/', views.task_delete, name='task-delete'),

    path('login/', auth_views.LoginView.as_view(template_name='tasks/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.signup, name='signup'),
]