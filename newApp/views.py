
from django.contrib.auth.forms import PasswordResetForm, UserCreationForm
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.views.generic import ListView, CreateView
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView

from .forms import PostForm
from django.shortcuts import render
from django.db.models import Q
from .models import  Post
#from newApp import models

class SignUpView(generic.CreateView):
    #model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class FeedPageView(ListView):
    model = Post
    template_name = 'newApp/feed.html'

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'newApp/post.html'
    success_url = reverse_lazy('home')

