# # Create your views here.
# from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
# from interface import models
# from interface.models import Contact
# from django.contrib import messages
# from interface.models import Forum_query, Reply
# from django.contrib.auth.decorators import login_required
# import crispy_forms
# from django.contrib.auth.signals import user_logged_in
# import requests
# import random 

# # Create your views here.
# def home(request):
#     if request.method=="POST":
#         name=request.POST['name']
#         email=request.POST['email']
#         message=request.POST['message']
#         contact= Contact(name=name,email=email,message=message)
#         contact.save()
#         messages.add_message(request,messages.SUCCESS,"Thank you for contacting us!")
#         messages.add_message(request,messages.SUCCESS,"You are very important to us, all information received will always remain confidential. We will connect with you as soon as we review your message.")
#     return render(request, 'index.html',{'title':'Farmfully-Home'})

# def predict(request):
#     return render(request, 'predict.html',{'title': 'Predict-Disease'})
    

# # @login_required_message(message="You should be logged in, in order to see the index!")
# @login_required(login_url= 'login')
# def forums(request):
#     # if request.method =='POST':
#     #     username=request.POST['username']
#     #     query=request.POST['query']
#     #     reply=request.POST['reply']
#     #     ins1 = Forum_query(username=username, query=query)
#     #     ins2 = Reply(reply=reply)
#     #     ins1.save()
#     #     ins2.save()
#     if request.method =='POST':
#         n=request.POST['isquery']
#         print(n)
#         if n=="0":
#             username=request.POST['username']
#             query=request.POST['query']
#             query_id=str(random.randint(1000000000,9999999999))
#             ins1 = Forum_query(username=username, query=query, query_id=query_id)
#             ins1.save()
#         else:
#             reply=request.POST['reply']
#             reply_id=request.POST['replyid']
#             ins2 = Reply(reply=reply, reply_id=reply_id)
#             ins2.save()
#     context={
#         'queries' : Forum_query.objects.all() ,   #accessing all the queries from the database
#         'replies':Reply.objects.all(),
#         'title':'Forums'
#     }
#     return render(request, 'forum.html', context)

# def learning(request):
#     return render(request, 'learning.html',{'title': 'E-Learning'})



# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from interface import models
from interface.models import Contact
from django.contrib import messages
from interface.models import Forum_query, Reply
from django.contrib.auth.decorators import login_required
import crispy_forms
from django.contrib.auth.signals import user_logged_in
import requests
import random 

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        message=request.POST['message']
        contact= Contact(name=name,email=email,message=message)
        contact.save()
        messages.add_message(request,messages.SUCCESS,"Thank you for contacting us!")
        messages.add_message(request,messages.SUCCESS,"You are very important to us, all information received will always remain confidential. We will connect with you as soon as we review your message.")
    return render(request, 'index.html',{'title':'Farmfully-Home'})

def predict(request):
    # if request.method=="POST":
    #     print("hi")
    #     response=requests.get('http://127.0.0.1:5000/').json()
    #     print(response)
    return render(request, 'predict.html',{'title': 'Predict-Disease'})
    

# @login_required_message(message="You should be logged in, in order to see the index!")
@login_required(login_url= 'login')
def forums(request):
    # if request.method =='POST':
    #     username=request.POST['username']
    #     query=request.POST['query']
    #     reply=request.POST['reply']
    #     ins1 = Forum_query(username=username, query=query)
    #     ins2 = Reply(reply=reply)
    #     ins1.save()
    #     ins2.save()
    if request.method =='POST':
        n=request.POST['isquery']
        print(n)
        if n=="0":
            username=request.POST['username']
            query=request.POST['query']
            query_id=str(random.randint(1000000000,9999999999))
            ins1 = Forum_query(username=username, query=query, query_id=query_id)
            ins1.save()
        else:
            reply=request.POST['reply']
            reply_id=request.POST['replyid']
            ins2 = Reply(reply=reply, reply_id=reply_id)
            ins2.save()
    context={
        'queries' : Forum_query.objects.all() ,   #accessing all the queries from the database
        'replies':Reply.objects.all(),
        'title':'Forums'
    }
    return render(request, 'forum.html', context)

def learning(request):
    return render(request, 'learning.html',{'title': 'E-Learning'})\
        
        
@csrf_exempt
def predict_process(request):
    # response=requests.get('http://127.0.0.1:5000/').json()
    if request.method =='POST':
        n=request.POST['prediction_result']
        print(n)
    return render(request,'predict_result.html',{'pred':n})