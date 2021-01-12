from rest_framework.permissions import SAFE_METHODS, BasePermission

# class isEmployer(BasePermission):
#     def has_permission(self, request, view, obj):
#         employer= request.obj.user.role== 'employer'

#         return bool(
#             super().has_permission(request, view)
#             and(employer)
#         ) 

def isEmployer(view_func):
    def wrapper_function(request, *args, **kwargs):
        user=request.user
        print(user)
        role=None
        if request.user.exists():
            role= request.user.role
        if role=='employer':
            return view_func(request, *args, **kwargs)
    return wrapper_function


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return request.user.is_staff
        

class IsAdmin(BasePermission): 
    def has_permission(self, request, view):
        employer = request.user.role == 'Employer'
        return bool(
             super().has_permission(request, view)
             and (employer)
            )      
