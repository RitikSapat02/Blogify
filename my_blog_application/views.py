from django.http import HttpResponse

def index(request):
    return HttpResponse("I am home page!")