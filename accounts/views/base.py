from rest_framework.exceptions import APIException
from rest_framework.views import APIView

from accounts.models import Group_Permissions, User_Groups
from companies.models import Employee, Enterprise


class Base(APIView):
    def get_enterprise_user(self, user_id):
        enterprise = {
            'is_owner': False,
            'permissions': []
        }

        enterprise['is_owner'] = Enterprise.objects.filter(
            user_id=user_id).exists()

        if enterprise['is_owner']:
            return enterprise


        #  PERMISSIONS, GET EMPLOYES
        employee = Employee.objects.filter(user_id=user_id).first()

        if not employee:
            raise APIException('Este usuário não é um funcionário')

        groups = User_Groups.objects.filter(user_id=user_id).all()

        for g in groups:
            # group.group.enterprise
            group = g.group
            permissions = Group_Permissions.objects.filter(
                group_id=group.id).all()

            for p in permissions:
                enterprise['permissions'].append({
                    'id': p.permission.id,
                    'label': p.permission.name,
                    'codename': p.permission.codename
                })

        return enterprise
