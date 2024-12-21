from rest_framework import permissions


class CheckStatus(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'hotel_owner':
            return False
        if request.user.role == 'client':
            return True



