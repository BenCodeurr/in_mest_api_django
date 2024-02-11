from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

# Create your views here.

def json_response(request):
    return JsonResponse({"name": "Lucky"})

def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")

def user_profile(request):
    return JsonResponse({
        "name": "TheOnlyBen",
        "email":"ben@gmail.com",
        "phone":"+243991735788"
        })


def filter_queries(request, id):
    query = {
        "id": id,
        "title": "Query",
        "description": "A test query",
        "status": "pending",
        "submitted_by": "Ben"
    }
        

    return JsonResponse(query)


class QueryView(View):
    queries = [
        {"id":1, "title":"Adama declined Val shots"},
        {"id":2, "title":"Samson declined Val shots"},
    ]
    def get(self, request):
        return JsonResponse({"result": self.queries})
    
    def post(self, request):
        return JsonResponse({"status": "ok"})