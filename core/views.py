from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse
from django.views import View


def health_chek(request):
    return JsonResponse({"ok": True}, status=200)


class AboutView(View):
    def get(self, request):
        return HttpResponse("Team Task Tracker API", content_type="text/plane", status=200)


def forbiden_view(request):
    return JsonResponse({"detail": "forbidden"}, status=403)
