from django.shortcuts import render

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer, SignInSerializer


class UserListApiView(APIView):
    ''' 유저 조회 API'''
    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)


class UserAPIView(APIView):
    ''' 유저 회원가입 및 수정, 탈퇴 API '''
    def post(self, request):
        user_serializer = UserCreateSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        user = User.objects.get(id=user_id)
        user_serializer = UserCreateSerializer(user, data=request.data, partial=True)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = User.objects.get(id=user_id)
        if user:
            user.delete()
            return Response({"message": "삭제 완료"}, status=status.HTTP_200_OK)
        return Response({"message": "유저가 없습니다."}, status=status.HTTP_400_BAD_REQUEST)


class SignInAPIView(APIView):
    ''' 로그인 API '''
    def post(self, request):
        login_serializer = SignInSerializer(data=request.data)

        if login_serializer.is_valid():
            token = login_serializer.validated_data
            return Response(
                {
                    "message": "로그인 성공!",
                    "access_token": token["access"],
                    "refresh_token": token["refresh"],
                },
                status=status.HTTP_200_OK,
            )
        return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
