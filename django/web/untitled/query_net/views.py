from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from query_net.main import test
def index(request):
    data = test.run()
    eturn render(request, 'index.html', {'data': data})

def hs(request):

    return render(request, 'hs.html')
