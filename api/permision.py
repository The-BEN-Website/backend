from rest_framework import permissions


class Pub(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        allowed_roles = ['ICT', 'PUBLICATION']
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.role in allowed_roles
    
class PublicationTeam(permissions.BasePermission):
    """
    Custom permission to only allow memebers of the publication team and ICT team have access to the particular endpoint
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            allowed_roles = ['ICT', 'PUBLICATION']
            if request.user.role in allowed_roles:
                return True
        return False

class MusicTeam(permissions.BasePermission):
    """
    Custom permission to only allow memebers of the music team and ICT team have access to the particular endpoint
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            allowed_roles = ['ICT', 'MUSIC']
            if request.user.role in allowed_roles:
                return True
        return False

class MediaTeam(permissions.BasePermission):
    """
    Custom permission to only allow memebers of the media team and ICT team have access to the particular endpoint
    """
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            allowed_roles = ['ICT', 'MEDIA']
            if request.user.role in allowed_roles:
                return True
        return False


# class HasRolePermission(permissions.BasePermission):
#     """
#     Custom permission to only allow users with specific roles to access the view.
#     """

#     allowed_roles = ['ICT', 'MEDIA']  # Add roles that should have access

#     def has_permission(self, request, view):
#         # Check if the user is authenticated and has the required role(s)
#         return (
#             request.user.is_authenticated
#             and request.user.role in self.allowed_roles
#         )


# class MessagePermission(permissions.BasePermission):
#     """
#     Custom permission to only allow users with specific roles to access the view.
#     """

#     def has_permission(self, request, view):
#         if request.user.is_authenticated and request.user.role == 'ICT':
#             return True
#         return False


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Assumes the model instance has an `owner` attribute.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Instance must have an attribute named `owner`.
        return obj.owner == request.user
    