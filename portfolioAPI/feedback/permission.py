from rest_framework import permissions

class ViewFeedback(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method == "POST":
            return True
        else:
            return False