from django.http import HttpResponse


def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META['HTTP_USER_AGENT']
    path = request.path

    return HttpResponse(f"""
    <p>Host: {host}</p>
    <p>User agent: {user_agent}</p>
    <p>Path: {path}</p>
    """, headers={"SecretCode": "1233463133"})
    


def about(request, name, age):
    return HttpResponse(f"<h3>Йоу, ты {name}, и тебе {age} лет, года, да хуй его знает</h3>")


def support(request):
    return HttpResponse("support")
