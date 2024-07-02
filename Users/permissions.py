from rest_framework import permissions

class FullDjangoModelPermissions(permissions.DjangoModelPermissions):
    def __init__(self) -> None:
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']



class ViewCustomerChangeArtworkPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('Users.allow_change_artwork')