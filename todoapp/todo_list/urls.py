from django.urls import path
from . import views

app_name = 'todo_list'

urlpatterns = [
    path('', views.todoPage, name='home'),
    path('createlist',views.createList, name='newlist'),
    path('showlist',views.showList, name='showlist'),
    path('addTodo/<int:head_id>',views.addTodo, name='addTodo'),
    path('createItem',views.createItem, name='createItem'),
    path('showInnerList/<int:p_id>',views.showInnerList, name='innerList'),
    path('email',views.email, name='email'),
    path('deleteList/<int:p_id>',views.deleteList,name='deleteList'),
    path('editList/<int:p1_id>',views.editList,name='editList'),
    path('saveEdit/<int:k_id>',views.saveEdit,name='saveEdit'),
    path('addnew/<int:head_id>',views.addnew, name='addnew')
]