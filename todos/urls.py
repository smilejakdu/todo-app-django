from django.urls import path
from .views      import (TodoView ,
                         TodoDetailView,
                         TodoUserView,
                         TodoTitleSearchView)

urlpatterns = [
    path(""              , TodoView.as_view()),
    path("mytodo"          , TodoUserView.as_view()),
    path("<int:todo_id>" , TodoDetailView.as_view()),
]
