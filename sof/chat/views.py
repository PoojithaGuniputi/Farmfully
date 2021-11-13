from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url= 'login')
def main_view(request):
    return render(request,"expert.html",{'title': 'Expert-Advice'})