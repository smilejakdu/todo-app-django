import json
import jwt
import re
import bcrypt
import requests

from .models                import User
from django.views           import View
from django.http            import HttpResponse, JsonResponse
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from todo_app.my_settings   import SECRET_KEY,   ALGORITHM


class SignUpView(View):
    def post(self , request):
        data = json.loads(request.body)

        try:
            for d in data:
                if not data[d]:
                    return JsonResponse({"message":f"doesnot_{d}"} , status = 400)

            validate_email(data['email'])

            if len(data['password']) < 5:
                return JsonResponse({"message":"SHORT_PASSWORD"} , status = 400)

            User(
                email    = data['email'],
                username = data['username'],
                password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            ).save()

            return HttpResponse(status = 200)


        except KeyError:
            return JsonResponse({"message" : "INVALID_KEY"},status = 400)

        except ValidationError:
            return HttpResponse(status=400)

        except Exception as e:
            return JsonResponse({"message" : e},status = 400)

class SignInView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            validate_email(data['email'])

            if User.objects.filter(email=data['email']).exists():
                user = User.objects.get(email=data['email'])

                if bcrypt.checkpw(data['password'].encode('utf-8'),
                                  user.password.encode('utf-8')):

                    token = jwt.encode({'email': data['email']},
                                           SECRET_KEY['secret'],
                                           algorithm=ALGORITHM).decode()

                    return JsonResponse({'access': token}, status=200, content_type="application/json")

                return HttpResponse(status=401)

            return HttpResponse(status=400)

        except KeyError:
            return JsonResponse({"message": "INVALID_KEYS"}, status=400)

        except User.DoesNotExist:
            return JsonResponse({"message": "INVALID_USER"}, status=400)

    def get(self , request):
        data = list(User.
                    objects.
                    values("email"))

        return JsonResponse({"data" : list(data)}, status = 200)

class TokenCheckView(View):
    def get(self , request):
        auth_token   = request.headers.get('Authorization', None)
        payload      = jwt.decode(auth_token,
                                  SECRET_KEY['secret'],
                                  algorithms = ALGORITHM)

        user         = User.objects.get(email = payload["email"])
        print("back user" , user.email)

        return JsonResponse({"data" : f"{user.email}" } , status = 200)
