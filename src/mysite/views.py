from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome</h1><a href="/polls/">Go to Polls</a>')
