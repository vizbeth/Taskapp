from django.urls import path
from . import views

urlpatterns = [
   path('edit/<task_id>', views.Edit_view, name='edit'),
   path('delete/<task_id>', views.delete_view, name='delete'),
   path('completed/<task_id>', views.completed, name='completed'),
   path('pending<task_id>', views.pending, name='pending')
]