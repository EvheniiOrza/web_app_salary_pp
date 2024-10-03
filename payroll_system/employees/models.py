from django.db import models

class Position(models.Model):
    position_title = models.CharField(max_length=45)
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)

class Employees(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    date_of_birth = models.DateField()
    hire_date = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    telegram_id = models.CharField(max_length=50, unique=True, null=True, blank=True)  # Telegram ID
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

class Salaries(models.Model):
    base_salary = models.DecimalField(max_digits=10, decimal_places=2)
    overtime_pay = models.DecimalField(max_digits=5, decimal_places=2)
    bonuses = models.DecimalField(max_digits=5, decimal_places=2)
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)

class Deductions(models.Model):
    deduction_type = models.CharField(max_length=45)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    deduction_date = models.DateField()
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)

class WorkTime(models.Model):
    work_date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2)
    employee = models.ForeignKey('Employees', on_delete=models.CASCADE)

class PayrollPeriods(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    payment_date = models.DateField()