import json
from .models         import Review
from products.models import Product
from account.models  import User
from account.utils   import login_check
from django.views    import View
from django.http     import HttpResponse, JsonResponse

class TodoView(View):
    @login_check
    def post(self ,request):
        return

    @login_check
    def get(self , request):
        return

class TodoDetailView(View):
    @login_check
    def post(self , request):
        return

    @login_check
    def delete(self , request):
        return

