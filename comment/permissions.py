from rest_framework.permissions import BasePermission

class IsStuff(BasePermission):
    message = "You are not allowed to access this resource."

    def has_permission(self, request):
        return bool(request.user and request.user.is_staff)
    
class IsOwner(BasePermission):
    def has_object_permission(self, request, obj):
        return request.user == obj.owner