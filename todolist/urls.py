from django.urls import path
from todolist.views import add_task, show_todolist_ajax, show_json
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import create_todo
from todolist.views import status
from todolist.views import delete

app_name = 'todolist'

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_todo, name="create_todo"),
    path('status/<int:id>/', status, name='status'),
    path('delete/<int:id>/', delete, name='delete'),
    path('json/', show_json, name="show_json"),
    path('add/', add_task, name="add_task"),
    path('', show_todolist_ajax, name='show_todolist_ajax'),
]