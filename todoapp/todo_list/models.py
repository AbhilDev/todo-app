from django.db import models

class TodoList(models.Model):
    head = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    def __str__(self):
        return self.head

class TodoApp(models.Model):                        #creating the category table
    todo_id = models.AutoField(primary_key=True)    #setting primarykey as todo_id
    category = models.CharField(max_length=50)      
    parent_id = models.IntegerField( default=0)
    def __str__(self):
        # todo_Id = int(todo_id)
        return self.category
