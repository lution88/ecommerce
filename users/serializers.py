from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "profile_img"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password", "mobile", "address", "profile_img"]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {
                'error_message':{
                    'required': '이메일을 다시 확인해주세요.',
                    'invalid': '알맞은 형식의 이메일을 입력해주세요.',
                },
                'required': True
            }
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.save()
        return user


