from django.urls import path
from . import views  # Імпортуємо views

urlpatterns = [
    path('employee/telegram/<str:telegram_id>/', views.employee_details, name='employee_details'),
]