from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound
from django_filters.rest_framework import DjangoFilterBackend

from todo.models import TodoTasks

from . import serializers, filters


class PublicTodoView(ListAPIView):
    """ Все публичные задачи """
    queryset = TodoTasks.objects.all()
    serializer_class = serializers.TodosAllSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TodoSimpleFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset\
            .filter(isPublic=True)\
            .order_by('-created_at', 'isImportant')


class PublicDetailView(APIView):
    """ Детали задача только публичные """
    def get(self, request, id):
        todo = TodoTasks.objects.filter(pk=id, isPublic=True).first()
        if not todo:
            raise NotFound(f'Задача с id={id} не найдена')
        serializer = serializers.TodoDetailsSerializer(todo)
        return Response(serializer.data)


class TodosAuthView(ListAPIView):
    """ Задачи авторизованных пользователей """
    permission_classes = (IsAuthenticated,)

    queryset = TodoTasks.objects.all()
    serializer_class = serializers.TodosSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.TodoAuthFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset \
            .filter(author=self.request.user) \
            .order_by('-created_at', 'isImportant')


class TodosAuthDetailView(ListAPIView):
    """ Детали задачи авторизованных пользователей """
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        todo = TodoTasks.objects.filter(pk=id, author=request.user).first()
        if not todo:
            raise NotFound(f'Задача с id={id} не найдена')
        serializer = serializers.TodoDetailsSerializer(todo)
        return Response(serializer.data)


class TodoAuthCreatorView(APIView):
    """ Добавление новой задчи для авторизованных пользователей """
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        todos = TodoTasks.objects.filter(author=request.user).order_by('-created_at', 'isImportant')
        serializer = serializers.TodosAllSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request):
        new_todo = serializers.TodoEditorSerializer(data=request.data)
        if new_todo.is_valid():
            new_todo.save(author=request.user)
            return Response(new_todo.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_todo.errors, status=status.HTTP_400_BAD_REQUEST)


class TodoAuthEditorView(APIView):
    """Удаление или изменение задачи для авторизованного пользователя """
    permission_classes = (IsAuthenticated, )

    def get(self, request, id):
        todo = TodoTasks.objects.filter(pk=id, author=request.user).first()
        if not todo:
            raise NotFound(f'Задача с id={id} не найдена')
        serializer = serializers.TodoDetailsSerializer(todo)
        return Response(serializer.data)

    def patch(self, request, id):
        todo = TodoTasks.objects.filter(pk=id, author=request.user).first()
        if not todo:
            raise NotFound(f'Задача с id={id} для пользователя {request.user.username} не найдена')

        new_todo = serializers.TodoEditorSerializer(todo, data=request.data, partial=True)
        if not new_todo.is_valid():
            return Response(new_todo.errors, status=status.HTTP_400_BAD_REQUEST)
        new_todo.save()

        return Response(new_todo.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        todo = TodoTasks.objects.filter(pk=id, author=request.user)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)