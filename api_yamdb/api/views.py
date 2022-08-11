import random

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, permissions, status, viewsets
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .permissions import IsAdminOrReadOnly, IsCustomAdminUser
from .serializers import (
    CategorySerializer, GenreSerializer, ObtainUserTokenSerializer,
    TitleSerializer, UserRegisterSerializer, UserSerializer)
from reviews.models import Category, Genre, Title

User = get_user_model()


class CreateListDestroyViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    pass


class CategoryViewSet(CreateListDestroyViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(CreateListDestroyViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')


class UserViewSet(viewsets.ModelViewSet):
    """ Вью сет для взаимодействия с пользователями с помощью админа. """

    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    permission_classes = (permissions.IsAuthenticated, IsCustomAdminUser,)
    lookup_field = 'username'
    lookup_value_regex = '[\w.@+-]{1,150}'
    search_fields = ('username',)
    queryset = User.objects.all()


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
                return Response({'access': token.access_token})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

