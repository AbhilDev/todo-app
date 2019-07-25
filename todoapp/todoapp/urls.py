from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todolist/', include('todo_list.urls')),
    path('signup/',include('signup.urls')),

]
