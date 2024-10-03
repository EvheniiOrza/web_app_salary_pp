from django.contrib import admin
from .models import Employees, Salaries, Position, Deductions, PayrollPeriods

admin.site.register(Employees)
admin.site.register(Salaries)
admin.site.register(Position)
admin.site.register(Deductions)
admin.site.register(PayrollPeriods)