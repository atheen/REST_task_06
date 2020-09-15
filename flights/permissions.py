from rest_framework.permissions import BasePermission
from datetime import date, timedelta

class IsOwner(BasePermission):
    message = "You're not the owner of the Booking"

    def has_object_permission(self, request, view, obj):
        if request.user.is_staff or obj.user == request.user:
            return True
        else:
            return False

class IsValid(BasePermission):
    message = "Booking is less than 3 days away."

    def has_object_permission(self, request, view, obj):
        if obj.date >= date.today()+timedelta(days=3):
            return True
        else:
            return False
