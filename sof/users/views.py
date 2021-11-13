from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import crispy_forms
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            Username = form.cleaned_data.get('Username')
            messages.add_message(request,messages.SUCCESS,"Your account has been successfully created! You are now able to login.")
            # return redirect('/login',{{'title':'Login'}})
            return redirect('/login')
    else:
        form=UserCreationForm()
    return render(request,'register.html',{'form':form})
