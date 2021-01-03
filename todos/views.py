import json

from .models      import Todo
from users.models import User
from users.utils  import login_check
from django.views import View
from django.http  import HttpResponse, JsonResponse

class TodoView(View):
    @login_check
    def post(self ,request):
        data = json.loads(request.body)
        print(data)
        try:
            for d in data:
                if not data[d]:
                    return JsonResponse({"message" : f"doesnot_{d}"} , status = 400)

            Todo(
                title   = data['title'],
                content = data['content'],
                user_id = request.user.id
            ).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({"message" : "invalid_key"} , status = 400)

        except Exception as e:
            return JsonResponse({"message" : e} , status = 400)

    def get(self , request):

        todo_data = Todo.objects.all().order_by('-created_at')

        try:

            data = {
                'data'           : [{
                    'id'         : todo.id,
                    'title'      : todo.title,
                    'content'    : todo.content,
                    'username'   : todo.user.username,
                    'created_at' : f"{todo.created_at.year}-{todo.created_at.month}-{todo.created_at.day}",
                }for todo in todo_data]}

            return JsonResponse({"data" : data} , status = 200)

        except Exception as e:
            return JsonResponse({"message" : e} , status = 400)

class TodoUserView(View):
    @login_check
    def get(self , request):
        try:
            todo_data = (User.
                         objects.
                         prefetch_related("todo_set").
                         get(id=request.user.id).
                         todo_set.all().order_by('-created_at'))

            data = {
                'data'           : [{
                    'id'         : todo.id,
                    'title'      : todo.title,
                    'content'    : todo.content,
                    'username'   : request.user.username,
                    'created_at' : f"{todo.created_at.year}-{todo.created_at.month}-{todo.created_at.day}",
                }for todo in todo_data]}

            return JsonResponse({"data" : data} , status = 200)

        except Exception as e:
            return JsonResponse({"message":e},status = 400)

class TodoDetailView(View):
    @login_check
    def post(self , request , todo_id):
        data = json.loads(request.body)
        print(data)
        try:
            for d in data:
                if not data[d]:
                    return JsonResponse({"message" : "doesnot_f{d}"} , status = 400)

            todo         = Todo.objects.get(id      = todo_id,
                                            user_id = request.user.id)

            todo.title   = data['title']
            todo.content = data['content']
            todo.save()

            return HttpResponse(status = 200)

        except Exception as e :
            return JsonResponse({"message":e} , status = 400)

    @login_check
    def delete(self , request , todo_id):

        try:
            if User.objects.filter(id = request.user.id).exists():
                todo = Todo.objects.get(id = todo_id)
                todo.delete()

                return HttpResponse(status = 200)

        except ValueError:
            return HttpResponse(status = 400)

        except Exception as e :
            return JsonResponse({"message" : e} , status = 400)

class SearchView(View):
    def get(self,request):
        query = request.GET.get("query",None)

        try:
            if len(query) > 0:

                todo_data = (Todo.
                             objects.
                             select_related("user").
                             filter(title__icontains = query).all())

                data = {
                    'data'         : [{
                        'id'       : todo.id,
                        'title'    : todo.title,
                        'content'  : todo.content,
                        'username' : todo.user.username,
                    }for todo in todo_data]}

                return JsonResponse({"data" : data} , status = 200)

        except ValueError:
            return JsonResponse({"message" : "invalid_error"} , status = 400)

        except Exception as e :
            return JsonResponse({"message" : e} , status = 400)


class MyListSearchView(View):
    @login_check
    def get(self,request):
        query = request.GET.get("query",None)

        try:
            if len(query) > 0:
                todo_data = (User.
                             objects.
                             prefetch_related("todo_set").
                             get(id=5).
                             todo_set.
                             filter(title__icontains=query).all())

                data = {
                    'data'           : [{
                        'id'         : todo.id,
                        'title'      : todo.title,
                        'content'    : todo.content,
                        'username'   : todo.user.username,
                        'created_at' : f"{todo.created_at.year}-{todo.created_at.month}-{todo.created_at.day}",
                    }for todo in todo_data]}

                return JsonResponse({"data" : data} , status = 200)

        except ValueError:
            return JsonResponse({"message" : "invalid_error"} , status = 400)

        except Exception as e :
            return JsonResponse({"message" : e} , status = 400)

