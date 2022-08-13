import random

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, filters, permissions, status
from rest_framework.decorators import action
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers import (UserSerializer, UserRegisterSerializer,
                             ObtainUserTokenSerializer, SelfUserSerializer)
from .permissions import IsCustomAdminUser, IsUserOrAdmin

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    """ Вью сет для взаимодействия с пользователями с помощью админа. """

    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (permissions.IsAuthenticated, IsCustomAdminUser,)
    lookup_field = 'username'
    lookup_value_regex = '[\w.@+-]{1,150}'
    search_fields = ('username',)
    queryset = User.objects.all()

    @action(detail=False, url_path='me', url_name='me',
            methods=('GET', 'PATCH'), permission_classes=[IsUserOrAdmin])
    def get_me(self, request, *args, **kwargs):
        """ Метод для обработки запросов к /me/"""

        queryset = User.objects.get(username=request.user)
        serializer = SelfUserSerializer(instance=queryset, data=request.data)
        if serializer.is_valid():
            # Если patch, то сохраняем данные пользователя
            if request.method == 'PATCH':
                serializer.save(**serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RegisterUser(CreateAPIView):
    """ Вью для самостоятельной регистрации пользователей. """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid():
            # Генерируем пятизначный код
            confirmation_code = random.randint(10000, 99999)
            User.objects.get_or_create(**serializer.validated_data,
                                       confirmation_code=confirmation_code)
            # Отправляем код на почту пользователя
            send_mail(
                'Confirmation code',
                f'Your confirmation code is {confirmation_code}',
                None,
                [serializer.validated_data.get('email')],
                fail_silently=False,
            )
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ObtainUserToken(CreateAPIView):
    """ Вью для получения JWT токена пользователем. """

    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = ObtainUserTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(
                User, username=serializer.data.get('username'))
            code = serializer.data.get('confirmation_code')
            # Проверяем, что код совпадает отправленный пользователем
            # и сгенерированный автоматически совпадает
            if user.confirmation_code == code:
                token = RefreshToken.for_user(user)
                return Response({'access': str(token.access_token)})
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
