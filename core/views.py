from django.http import JsonResponse, HttpResponse
from django.views import View
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny


@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    return JsonResponse({"ok": True}, status=200)


class AboutView(View):
    def get(self, request):
        return HttpResponse("Team Task Tracker API", status=200, content_type="text/plain")


@api_view(['GET'])
@permission_classes([AllowAny])
def forbidden_view(request):
    return JsonResponse({"detail": "forbidden"}, status=403)
