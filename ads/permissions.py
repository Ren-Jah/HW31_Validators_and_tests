from rest_framework import permissions

from users.models import UserRole


class IsOwnerSelection(permissions.BasePermission):
    message = 'Редактировать и удалять подборку может только владелец.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == obj.owner:
            return True
        return False


class IsOwnerAdOrStaff(permissions.BasePermission):
    message = 'Вы не являетесь владельцем или модератором/админом.'

    def has_object_permission(self, request, view, obj):
        if request.user.role == obj.author or request.user.role in [UserRole.ADMIN, UserRole.Moderator]:
            return True
        return False
