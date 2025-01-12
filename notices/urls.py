from django.urls import path
from . import views

urlpatterns = [
    path('', views.notice_list, name='notice_list'),
    path('notice/add/', views.notice_add, name='notice_add'),
    path('notice/<int:notice_id>/edit/', views.notice_edit, name='notice_edit'),
    path('notice/<int:notice_id>/delete/', views.notice_delete, name='notice_delete'),
    path('notice/<int:notice_id>/pin/', views.notice_pin, name='notice_pin'),
    path('notice/<int:notice_id>/', views.notice_detail, name='notice_detail'),
]