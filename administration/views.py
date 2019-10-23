from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Client
from .forms import ClientForm, UserForm
from django.shortcuts import redirect
from django.conf import settings
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
# from rest_framework import viewsets
# from .serializers import UserSerializer
# from rest_framework.permissions import IsAuthenticated

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)


# Create your views here.
class GetClient(LoginRequiredMixin, View):
    def get(self, request):
        clients = Client.objects.all()
        return render(request, 'alerts.html', {'clients': clients})

class GetUser(LoginRequiredMixin, View):
    def get(self, request):
        user_form = UserForm()
        users = User.objects.all()
        return render(request, 'administration.html', {'users': users, 'user_form': user_form})

    def post(self, request):
        if request.method == "POST":
            user_form = UserForm(request.POST)
            if user_form.is_valid():
                usuario = user_form.save(commit=False)
                usuario.set_password(usuario.password)
                usuario.save()
                return redirect('get_users')
        
        # return render(request, 'administration.html', {'users': users, 'user_form': user_form})
        return render(request, 'administration.html', {'user_form': user_form})

    # def post(self, request):
    #     user_form = UserForm(request.POST)
    #     if user_form.is_valid():
    #         user = user_form.save(commit=False)
    #         user.username = user.username
    #         user.save()
    #     print(user_form)
    #     return redirect('get_users')