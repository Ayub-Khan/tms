"""Views for order application."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.views import View

from employee.forms import EmployeeForm
from employee.models import Employee
from order.models import Task


class EmployeeListView(LoginRequiredMixin, View):
    """List all employees."""

    def get(self, request):
        """Render employee list template.."""
        employees = Employee.objects.all()
        task_groupby_employee = Task.objects.all().values('employee').annotate(total=Count('employee'))
        employee_with_no_of_tasks = {emp_task['employee']: emp_task['total'] for emp_task in task_groupby_employee}
        context = {
            'employees': employees,
            'employee_task_dict': employee_with_no_of_tasks
        }
        return render(request, 'employee/list-employees.html', context)


employee_list_view = EmployeeListView.as_view()


class EmployeeDetailView(LoginRequiredMixin, View):
    """Class based view for Employee for detail of Employee."""

    def get(self, request, id):
        """Render Employee detail tempalte.."""
        employee = Employee.objects.get(id=id)
        context = {
            'employee': employee,
            'tasks': Task.objects.filter(employee=employee)
        }
        return render(request, 'employee/employee-detail.html', context)


employee_detail_view = EmployeeDetailView.as_view()


class EmployeeAddView(LoginRequiredMixin, View):
    """Class based view for adding new Employee."""

    def get(self, request):
        """Return add new Employee form."""
        form = EmployeeForm()
        return render(request, 'employee/add-employee.html',
                      {'form': form, 'func': 'Add'})

    def post(self, request):
        """Save employee and redirect to employee list."""
        form = EmployeeForm(request.POST)
        if form.is_valid():
            new_employee = form.save()
            return redirect('employee:employee_detail', id=new_employee.id)
        else:
            return render(request, 'employee/add-employee.html', {'form': form, 'func': 'Add'})


employee_add_view = EmployeeAddView.as_view()


class EmployeeUpdateView(LoginRequiredMixin, View):
    """Class based view for adding new Employee."""

    def get(self, request, id):
        """Return add new Employee form."""
        employee = get_object_or_404(Employee, id=id)
        form = EmployeeForm(instance=employee)
        return render(request, 'employee/add-employee.html',
                      {'form': form, 'func': 'Update', 'employee': employee})

    def post(self, request, id):
        """Save employee and redirect to employee list."""
        employee = get_object_or_404(Employee, id=id)
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            new_employee = form.save()
            return redirect('employee:employee_detail', id=new_employee.id)
        else:
            return render(request, 'employee/add-employee.html', {'form': form, 'func': 'Update', 'employee': employee})


employee_update_view = EmployeeUpdateView.as_view()


class EmployeeDeleteView(LoginRequiredMixin, View):
    """Class based view for deleting Employee."""

    def post(self, request):
        """Delete employee."""
        id = request.POST.get('id')
        employee = get_object_or_404(Employee, id=id)
        employee.delete()
        return redirect('employee:employees')


employee_delete_view = EmployeeDeleteView.as_view()
