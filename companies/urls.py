from django.urls import path

from companies.views.employees import EmployeeDatail, Employees
from companies.views.groups import GroupDetail, Groups
from companies.views.permissions import PermissionDetail
from companies.views.tasks import TaskDetail, Tasks

urlpatterns = [
    # Employees endpoints
    path('employees', Employees.as_view()),
    path('employees/<int:employee_id>', EmployeeDatail.as_view()),

    #  Groups and Permissions Endpoints
    path('groups', Groups.as_view()),
    path('groups/<int:group_id>', GroupDetail.as_view()),

    path('permissions', PermissionDetail.as_view()),

    #  Tasks endpoints
    path('tasks', Tasks.as_view()),
    path('tasks/<int:task_id>', TaskDetail.as_view()),

]
