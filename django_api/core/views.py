from rest_framework.viewsets import ViewSet
from django.http import HttpResponse

class HelloWorldViewSet(ViewSet):
    def list(request, *args, **kwargs):
        return HttpResponse("Hello World!")
