from django.shortcuts import render
from django.contrib.auth import logout
from rest_framework import generics
from .serializers import *
from ..core.models import *
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class ListScreenshotView(generics.ListCreateAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

class ListTrackedSiteView(generics.ListCreateAPIView):
    queryset = TrackedSite.objects.all()
    serializer_class = TrackedSerializer

class ListSiteView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class ListSuggestedSiteView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SuggestedSite.objects.all()
    serializer_class = SuggestedSiteSerializer

class ListCategoryView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ListProfileView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        profiles = User.objects.all()
        data = ProfileSerializer(profiles, many=True).data
        return Response(data)

class TrackedSiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = TrackedSite.objects.all()
    serializer_class = TrackedSerializer

class ScreenshotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Screenshot.objects.all()
    serializer_class = ScreenshotSerializer

class SiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SuggestedSiteDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = SuggestedSite.objects.all()
    serializer_class = SuggestedSiteSerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProfileDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request, pk):
        profile = get_object_or_404(Profile, pk=pk)
        data = ProfileSerializer(profile).data
        return Response(data)

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {
            'username':request.user.username,
            'admin':request.user.is_staff
        }
        return Response(content)

class LogoutUserView(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        logout(request)
        content = {
            "message":"You've been logged out succesfully."
        }
        return Response(content)