from django.urls import path, include
from . import views


urlpatterns = [
    # Authentication
    path('', include('rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('login/', include('djoser.urls.authtoken')),
    # url rest
    path('notes/', views.note_list, name='note_list'),
    path('users/', views.users_list, name='user_list'),
    path('detail/<str:pk>/', views.note_detail, name='note_detail'),
    path('create/', views.note_create, name='note_create'),
    path('update/<str:pk>/', views.note_update, name='note_update'),
    path('delete/<str:pk>/', views.note_delete, name='note_delete'),
]
