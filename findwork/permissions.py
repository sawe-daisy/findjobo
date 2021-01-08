from rest_framework.permissions import SAFE_METHODS, BasePermission
class isEmpoloyer(BasePermission):
    def has_permission(self, request, view):
        employer= request.user.role == 'employer'

        return bool(
            super().has_permission(request, view)
            and(merchant)
        ) 