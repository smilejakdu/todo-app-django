import json
from .models         import Todo
from products.models import Product
from account.models  import User
from account.utils   import login_check
from django.views    import View
from django.http     import HttpResponse, JsonResponse

class TodoView(View):
    @login_check
    def post(self ,request , user_id):
        data = json.loads(request.body)

        try:
            for d in data:
                if not data[d]:
                    return JsonResponse({"message" : f"doesnot_{d}"} , status = 400)

            Todo(
                title       = data['title'],
                description = data['description'],
                user_id     = user_id
            ).save()

            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({"message" : "invalid_key"} , status = 400)

        except Exception as e:
            return JsonResponse({"message" : e} , status = 400)

    def get(self , request):

        try:
            data = (Todo.
                    objects.
                    values())
            return JsonResponse({"data" : list(data)} , status = 200)

        except Exception as e:
            return JsonResponse({"message" : e} , status = 400)

class TodoDetailView(View):
    @login_check
    def post(self , request):
        return

    @login_check
    def delete(self , request):
        return

