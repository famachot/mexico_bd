# -*- coding: utf-8 -*-
from rest_framework import permissions


class IsStaff(permissions.BasePermission):
	def has_permission(self, request, view):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return request.user.is_staff

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS:
			return True
		else:
			return request.user.is_staff