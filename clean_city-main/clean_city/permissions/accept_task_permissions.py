from rest_framework import permissions


class IsCleaner(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_cleaner

class IsGarbageCollector(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_bin_collector
