from django_filters import rest_framework as filters

from todo.models import TodoTasks


class TodoAuthFilter(filters.FilterSet):
    class Meta:
        model = TodoTasks
        fields = [
            'status',
            'isImportant',
            'isPublic',
        ]


class TodoSimpleFilter(filters.FilterSet):
    class Meta:
        model = TodoTasks
        fields = [
            'status',
            'isImportant',
        ]