from django.urls import path
from todoApi import views

urlpatterns = [
    path('pub_todos/',                  views.PublicTodoView.as_view(),      name='Все публичные задачи'),
    path('pub_todo/<int:id>/',          views.PublicDetailView.as_view(),    name='Детали по задаче'),
    path('auth_todos/',                 views.TodosAuthView.as_view(),       name='Все мои задачи'),
    path('auth_todo/<int:id>/',         views.TodosAuthDetailView.as_view(), name='Детали по моей задаче'),
    path('auth_todo/add/',              views.TodoAuthCreatorView.as_view(), name='Добавить новую'),
    path('auth_todo/<int:id>/edit/',    views.TodoAuthEditorView.as_view(),  name='Редактировать существующую'),
]
