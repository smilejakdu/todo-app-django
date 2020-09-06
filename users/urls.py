from django.urls import path, include
from .views      import (SignUpView,
                         SignInView,
                         TokenCheckView)

urlpatterns = [
    path("signup" , SignUpView.as_view()),
    path("signin" , SignInView.as_view()),
    path("token"  , TokenCheckView.as_view()),
]

