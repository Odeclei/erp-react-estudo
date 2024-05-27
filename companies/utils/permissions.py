# flake8: noqa
from django.contrib.auth.models import Permission
from rest_framework import permissions

from accounts.models import Group_Permissions, User_Groups


def check_permissions(user, method, permissions_to):
    if not user.is_authenticated:
        return False

    if user.is_owner:
        return True

    required_permission = 'view_'+permissions_to
    if method == 'POST':
        required_permission = 'add_'+permissions_to
    elif method == 'PUT':
        required_permission = 'change_'+permissions_to
    elif method == 'DELETE':
        required_permission = 'delete_'+permissions_to

    groups = User_Groups.objects.values(
        'group_id').filter(user_id=user.id).all()

    for group in groups:
        permissions = Group_Permissions.objects.values(
            'permission_id').filter(group_id=group['group_id']).all()
        for permission in permissions:
            if Permission.objects.filter(
                    id=permission['permission_id'],
                    codename=required_permission).exists():
                return True


class EmployeesPermission(permissions.BasePermission):
    message = 'O funcionário não tem permissão para gerenciar.'

    def has_permission(self, request, _view):
        return check_permissions(request.user, request.method, permissions_to='employee')


class GroupsPermissions(permissions.BasePermission):
    message = 'O funcionário não tem permissão para gerenciar os grupos.'

    def has_permission(self, request, _view):
        return check_permissions(request.user, request.method, permissions_to='group')


class GroupsPermissionsPermission(permissions.BasePermission):
    message = 'O funcionário não tem liberação para gerenciar as permissões.'

    def has_permission(self, request, _view):
        return check_permissions(request.user, request.method, permissions_to='permission')


class TaskPermission(permissions.BasePermission):
    message = 'O funcionário não tem permissão para gerenciar as tarefas.'

    def has_permission(self, request, _view):
        return check_permissions(request.user, request.method, permissions_to='task')
