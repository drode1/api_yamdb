from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from rest_framework.validators import UniqueValidator

from reviews.models import Category, Genre, Title, GenreTitle

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TitleSerializer(serializers.ModelSerializer):
    category = SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all(),
    )
    genre = SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        slug_field='slug'
    )

    class Meta:
        fields = '__all__'
        model = Title


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с пользователями через права админа. """

    # Переопределяем почту, чтобы проверять уникальность значений.
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all(),
            message='Пользователь с такой почтой уже существует.')]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email', 'first_name', 'last_name', 'bio', 'role',
        )


class UserRegisterSerializer(serializers.Serializer):
    """Сериализатор для проверки данных пользователей при самостоятельной
    регистрации через токен. """

    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(queryset=User.objects.all())])

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())])

    def validate(self, data):
        # Проверяем, что username не является me
        if data['username'] == 'me':
            raise serializers.ValidationError("Me is invalid username")
        return data


class ObtainUserTokenSerializer(serializers.Serializer):
    """Сериализатор для получения токена, когда пользователь уже
    зарегистрирован. """

    username = serializers.CharField(max_length=150)
    confirmation_code = serializers.IntegerField()
