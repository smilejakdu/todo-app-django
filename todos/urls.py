from django.urls import path
from .views      import (TodoView ,
                         TodoDetailView)

urlpatterns = [
    path(""              , TodoView.as_view()),
    path("<int:todo_id>" , TodoDetailView.as_view()),
]
