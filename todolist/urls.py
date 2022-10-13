# TODO: Implement Routings Here
from django.urls import path
from todolist.views import show_todolist, register, login_user, logout_user, create_task, update_task, delete_task, add_task, show_json

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create_task'),
    path('update_task/<int:pk>/', update_task, name='update_task'),
    path('delete_task/<int:pk>/', delete_task, name='delete_task'),
    path('json/', show_json, name='show_json'),
    path('add/', add_task, name='add_task'),

]