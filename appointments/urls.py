from django.urls import path
from . import views

app_name = 'appointments'

urlpatterns = [
    path('book/', views.book_appointment, name='book'),
    path('history/', views.appointment_history, name='history'),
    path('cancel/<int:pk>/', views.appointment_cancel, name='cancel'),
]
