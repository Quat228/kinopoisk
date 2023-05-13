from rest_framework import serializers

from . import models


class UserRegisterSerializer(serializers.ModelSerializer):
    password_check = serializers.CharField(write_only=True)

    class Meta:
        model = models.User
        fields = ['username', 'password', 'password_check', 'profile_image']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
        if data['password'] != data['password_check']:
            raise serializers.ValidationError('Пароли не совпадают!')
        return data

    def validate_password(self, value):
        special_chars = '[!@#$%^&*(),.?":{}|<>]'
        if len(value) < 8:
            raise serializers.ValidationError('Пароль должен содержать как минимум 8 символов!')
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError('Пароль должен содержать хотя бы одну цифру')
        if not any(char.islower() for char in value) or not any(char.isupper() for char in value):
            raise serializers.ValidationError('Пароль должен содержать одну одну заглавную и одну прописную букву')
        if not any(char in special_chars for char in value):
            raise serializers.ValidationError(f'Пароль должен содержать хотя бы '
                                              f'один специальный символ: {special_chars}')
        return value

    def create(self, validated_data):
        user = models.User(
            username=validated_data['username']
        )
        profile_image = validated_data.get('profile_image')
        if profile_image:
            user.profile_image = profile_image
        user.set_password(validated_data['password'])
        user.save()
        try:
            profile = models.Profile.objects.create(
                user=user
            )
        except Exception as e:
            user.delete()
            raise e
        else:
            return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = '__all__'
        read_only_fields = ['user', ]
