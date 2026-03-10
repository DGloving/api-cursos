from rest_framework import permissions


class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        
        if hasattr(obj, 'instructor'):
            return obj.instructor == request.user
        
        if hasattr(obj, 'course'):
            return obj.course.instructor == request.user
            
        
        return False