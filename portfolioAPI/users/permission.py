from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Class which allows user to update edit/update their own profile"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return False