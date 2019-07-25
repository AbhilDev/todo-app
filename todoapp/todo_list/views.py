from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import *
from django.conf import settings
from django.core.mail import send_mail

def todoPage(request):
    return render(request, 'todo_list/index.html')

def createList(request):
    return render(request, 'todo_list/createlist.html')

def showList(request):
    items = TodoApp.objects.all()
    return render(request, 'todo_list/showlist.html',{'key':items})



#saving the head and render to next page
def createItem(request):
    new_head = request.POST['head']             #getting the post data from the input field named head in html page
    new_Head = TodoApp(category = new_head )       #assign the data to the head in the model TodoList
    new_Head.save()                             #saving the changes
    head_id = new_Head.todo_id                           #getting the new_head
    # test=TodoList.objects.get(head = new_head ) #getting the new_head
    # print(test.id)                              #printing the id
    return render(request,'todo_list/createItem.html',{"head_id":head_id})
#-----------------------------------------------------------------------------------------------------

def addTodo(request,head_id):
    if request.method=='POST':
        new_content = request.POST['content']   #getting the post data from the input field named content in the html page
        new_Content = TodoApp(category = new_content,parent_id = head_id) 
        #the new content is saved in to the category and the head_id is saved as the parent id.
        new_Content.save()
        if request.POST.get('save_and_add'):
                return render(request,'todo_list/createItem.html',{"head_id":head_id})
        else:
                return HttpResponseRedirect('../')
                


def showInnerList(request,p_id):
        head = TodoApp.objects.get(todo_id=p_id)
        items = TodoApp.objects.filter(parent_id=p_id)
        return render(request, 'todo_list/showinnerlist.html',{'key':items,'key1':head})

def email(request):
        # subject = 'Hi bro, you are very lucky'
        # recipient_list = ['abhildevdevalal@gmail.com',]
        # from_email = settings.DEFAULT_FROM_EMAIL
        # send_mail(subject, "message", from_email , recipient_list)
        send_mail('Subject here','Here is the message.','iamdk.devkrishna@gmail.com',['abhildevdevalal@gmail.com','pajila@gmail.com','iamdk.devkrishna@gmail.com'])
        return HttpResponse('Mail has been sent')

def deleteList(request,p_id):
        item = TodoApp.objects.get(todo_id=p_id)
        parent_id =item.parent_id
        item.delete()
        return redirect('todo_list:innerList',p_id=parent_id)
        
def editList(request,p1_id):
        head = TodoApp.objects.get(todo_id=p1_id)
        items = TodoApp.objects.filter(parent_id=p1_id)
        return render(request, 'todo_list/edit.html',{'key':items,'key1':head,'p1_id':p1_id})

def saveEdit(request,k_id):
        if request.method=='POST':
                new_content = request.POST['content']
                temp = TodoApp.objects.get(todo_id=k_id)
                temp.category = new_content
                temp.save()
                parent_id = temp.parent_id
        return redirect('todo_list:editList',p1_id=parent_id)

def addnew(request,head_id):
        h_id=head_id
        return render(request,'todo_list/createItem.html',{"head_id":h_id})
        