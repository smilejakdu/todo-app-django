from django.urls import path
from .views      import (TodoView ,
                         TodoDetailView,
                         TodoUserView,
                         SearchView ,
                         MyListSearchView)

urlpatterns = [
    path(""              , TodoView.as_view()),
    path("mytodo"        , TodoUserView.as_view()),
    path("search"        , SearchView.as_view()),
    path("mylistsearch"  , MyListSearchView.as_view()),
    path("<int:todo_id>" , TodoDetailView.as_view()),
]
