from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Url
from .serializers import UrlSerializer
from .UrlCreater import UrlCreater


class ShortUrlCreateView(APIView):
    def post(self, request):
        url = UrlSerializer(data=request.data)
        if url.is_valid():
            url = UrlCreater(url.data["httpurl"])()
            url.save()
            return Response(url.short_url)
        return Response(url.errors)


class ShortUrlRedirectview(APIView):
    def get(self, request, short_id):
        url = get_object_or_404(Url, pk=short_id)
        url.save()
        return HttpResponseRedirect(url.httpurl)
