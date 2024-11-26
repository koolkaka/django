from django.urls import path
from .views import VlogListView, VlogDetailView, VlogCreateView, VlogUpdateView, VlogDeleteView, register, CustomLoginView, profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', VlogListView.as_view(), name='vlog_list'),
    path('<int:pk>/', VlogDetailView.as_view(), name='vlog_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('new/', VlogCreateView.as_view(), name='vlog_create'),
    path('edit/<int:pk>/', VlogUpdateView.as_view(), name='vlog_update'),
    path('delete/<int:pk>/', VlogDeleteView.as_view(), name='vlog_delete'),
    path('profile/', profile, name='profile'),
]