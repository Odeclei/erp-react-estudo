from django.contrib.auth.models import Permission
from rest_framework.response import Response

from companies.serializers import PermissionsSerializers
from companies.utils.permissions import GroupsPermissions
from companies.views.base import Base


class PermissionDetail(Base):
    permission_classes = [GroupsPermissions]

    def get(self, request):
        # auth - permission (2)
        # accounts - group (7)
        # companies - employee (12)
        # companies - task (13)
        permissions = Permission.objects.filter(
            content_type_id__in=[2, 7, 12, 13]).all()
        serializer = PermissionsSerializers(permissions, many=True)

        return Response({'permission': serializer.data})
