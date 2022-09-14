from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """유저 조회 serializer"""

    class Meta:
        model = User
        fields = ["id", "username", "email", "profile_img"]


class UserCreateSerializer(serializers.ModelSerializer):
    """유저 생성, 조회, 삭제 serializer"""

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "password",
            "mobile",
            "address",
            "profile_img",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {
                "error_messages": {
                    "required": "이메일을 다시 확인해주세요.",
                    "invalid": "알맞은 형식의 이메일을 입력해주세요.",
                },
                "required": True,
            },
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance


class SignInSerializer(TokenObtainPairSerializer):
    """로그인 serializer"""

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        user = User.objects.get(email=email)

        if user:
            if not user.is_active:
                raise serializers.ValidationError("비활성화된 계정입니다.")
            if not user.check_password(password):
                raise serializers.ValidationError("비밀번호를 다시 확인해주세요..")
        else:
            raise serializers.ValidationError("없는 계정입니다. 다시 확인해주세요.")

        token = super().get_token(user)
        access_token = str(token.access_token)
        refresh_token = str(token)

        data = {
            "access": access_token,
            "refresh": refresh_token,
        }
        return data
