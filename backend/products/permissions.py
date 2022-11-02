from rest_framework import permissions


class IsStaffEditorPermission(permissions.DjangoModelPermissions):

    # or if you want to provide custom permission codes.
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s',],
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    # def has_permission(self, request, view):
    #     if not request.user.is_staff:
    #         return False
    #     return super().has_permission(request, view)
    
    # def has_permission(self, request, view):
    #     user = request.user
    #     if user.is_staff:
    #         if user.has_perm("products.add_product"): # app_name._action_model_name
    #             return True
    #         if user.has_perm("products.view_product"):
    #             return True
    #         if user.has_perm("products.change_product"):
    #             return True
    #         if user.has_perm("products.delete_product"):
    #             return True
    #         return True
    #     print(user.get_all_permission)
    #     return False

    # def has_object_permission(self, request, view, obj):
    #     return obj.owner == request.user
