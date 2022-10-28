from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import *


class LoginView(View):

    def get(self,request):


            return render(request,'login.html')
    def post(self, request):
        user = authenticate(username=request.POST.get('login'),
                            password = request.POST.get('password'))

        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/maqola/')

class LogoutView(View):
    def get(self,request):
        return redirect('/')

class RegisterView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        return redirect('/')
class BlogView(View):
    def get(self,request):

        data = {
            'lessons':Mavzu.objects.filter(user=request.user)
        }
        return render(request,'maqola.html',data)
    def post(self,request):

        Mavzu.objects.create(
            sarlavha = request.POST.get('s'),
            sana = request.POST.get('d'),
            matn = request.POST.get('t'),
            m_mavzu = request.POST.get('m'),
            )
        return redirect('/maqola/')

class TanlanganView(View):
    def get(self,request,pk):
        data = {
            'lessons': Mavzu.objects.filter(id=pk)

        }
        return render(request,'tanlan.html',data)





