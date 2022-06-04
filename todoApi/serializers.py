from datetime import datetime
from django.contrib.auth.models import User
from rest_framework import serializers

from todo.models import TodoTasks


class TodoAuthorSerializer(serializers.ModelSerializer):
    """ Автор задачи """
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'date_joined')

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        date_joined = datetime.strptime(ret['date_joined'], '%Y-%m-%dT%H:%M:%S.%fZ')
        ret['date_joined'] = date_joined.strftime('%d %B %Y %H:%M:%S')
        return ret


class TodosSerializer(serializers.ModelSerializer):
    """ Задачки """
    # Меняем вывод, вместо `ID` пользователя будет `Имя`
    author = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        model = TodoTasks
        fields = "__all__"

    def to_representation(self, instance):
        """ Переопределение вывода. Меняем формат даты в ответе """
        ret = super().to_representation(instance)
        created_at = datetime.strptime(ret['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
        ret['created_at'] = created_at.strftime('%d %B %Y %H:%M:%S')
        resolutionDate = datetime.strptime(ret['resolutionDate'], '%Y-%m-%dT%H:%M:%SZ')
        ret['resolutionDate'] = resolutionDate.strftime('%d %B %Y %H:%M:%S')
        return ret


class TodoDetailsSerializer(serializers.ModelSerializer):
    """ Одна задача """

    author = TodoAuthorSerializer

    class Meta:
        model = TodoTasks
        exclude = ('isPublic', )  # Исключить поле

    # def to_representation(self, instance):
    #     """ Переопределение вывода. Меняем формат даты в ответе """
    #     ret = super().to_representation(instance)
    #     created_at = datetime.strptime(ret['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ')
    #     ret['created_at'] = created_at.strftime('%d %B %Y %H:%M:%S')
    #     resolutionDate = datetime.strptime(ret['resolutionDate'], '%Y-%m-%dT%H:%M:%SZ')
    #     ret['resolutionDate'] = resolutionDate.strftime('%d %B %Y %H:%M:%S')
    #     return ret


class TodoEditorSerializer(serializers.ModelSerializer):
    """ Добавление или изменение задачи """

    author = TodoAuthorSerializer

    class Meta:
        model = TodoTasks
        fields = "__all__"


class TodosAllSerializer(serializers.ModelSerializer):
    """ Задачки """
    # Меняем вывод, вместо `ID` пользователя будет `Имя`
    #author = TodoAuthorSerializer(read_only=True)

    class Meta:
        model = TodoTasks
        fields = ('id', 'title', 'description', 'created_at', 'resolutionDate')



