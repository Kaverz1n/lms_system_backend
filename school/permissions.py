from rest_framework.permissions import BasePermission


class IsModeratorOrOwner(BasePermission):
    '''
    Кастомное разрешение для проверки пользователя на модератора
    или владельца объекта
    '''

    def has_permission(self, request, view):
        group = request.user.groups.filter(name='moderator').exists()

        if group:
            return request.method not in ['POST', 'DELETE']

        return True

    def has_object_permission(self, request, view, obj):
        group = request.user.groups.filter(name='moderator').exists()

        if group:
            return request.method in ['GET', 'PUT', 'PATCH']

        return request.user == obj.user
