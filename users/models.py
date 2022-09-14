from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser

from core.models import TimeStampModel


class UserManager(BaseUserManager):
    """User 생성 시 기본 세팅"""

    # 일반 유저 생성
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError("유저네임은 필수입니다.")
        user = self.model(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    # super 유저 생성
    def create_superuser(self, username, email, password):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, TimeStampModel):
    email = models.EmailField("이메일", unique=True)
    username = models.CharField("유저네임", max_length=50)
    password = models.CharField("비밀번호", max_length=255)
    mobile = models.CharField("전화번호", max_length=20)
    address = models.CharField("주소", max_length=200)
    profile_img = models.ImageField("프로필이미지", upload_to="", blank=True)

    is_active = models.BooleanField("계정활성화", default=True)
    is_admin = models.BooleanField("관리자", default=False)
    is_staff = models.BooleanField("판매자", default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    def __str__(self):
        return f'{self.username} / {self.email}'
