from django.urls import path
from django.urls.conf import include
from . import views
from .views import CreatePostView, SignUpView
import newApp


urlpatterns = [
    path('registration/signup/',SignUpView.as_view(), name='signup'),
    

    
]
