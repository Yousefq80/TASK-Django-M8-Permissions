from rest_framework.permissions import BasePermission
from datetime import date, timedelta
 
class IsOwner(BasePermission):
    message = "You are not Authorize to Access"
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or obj.user == request.user

class UpdateCancel(BasePermission):
    message = "You can not update/cancel a booking only before 3 days of the Depature"
    
    def has_object_permission(self, request, view, obj):
        return (obj.date - date.today()).days> 3