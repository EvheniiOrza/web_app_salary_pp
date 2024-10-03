from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Employees, Salaries


def employee_details(request, telegram_id):
    # Знаходимо працівника за його Telegram ID
    employee = get_object_or_404(Employees, telegram_id=telegram_id)

    # Знаходимо зарплату цього працівника
    salary = get_object_or_404(Salaries, employee=employee)

    # Розраховуємо загальну суму зарплати
    total_salary = salary.base_salary + salary.overtime_pay + salary.bonuses

    context = {
        'employee': employee,
        'salary': salary,
        'total_salary': total_salary
    }

    # Відображаємо шаблон з даними
    return render(request, 'employee_details.html', context)
