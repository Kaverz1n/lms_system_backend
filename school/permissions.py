from rest_framework.permissions import BasePermission


class IsModeratorOrOwner(BasePermission):
    '''
    Кастомное разрешение для проверки пользователя на модератора
    или владельца объекта
    '''

    def has_permission(self, request, view):
        moderator = request.user.groups.filter(name='moderator').exists()
        teacher = request.user.groups.filter(name='teacher').exists()
        admin = request.user.is_superuser

        if moderator:
            return request.method not in ['POST', 'DELETE']
        elif teacher or admin:
            return True

        return request.method in ['GET']

    def has_object_permission(self, request, view, obj):
        moderator = request.user.groups.filter(name='moderator').exists()
        teacher = request.user.groups.filter(name='teacher').exists()
        admin = request.user.is_superuser

        if moderator:
            return request.method in ['GET', 'PUT', 'PATCH']
        elif teacher:
            return request.user == obj.user
        elif admin:
            return True

        return request.method in ['GET']
