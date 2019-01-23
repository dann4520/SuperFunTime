from django.shortcuts import render

# Create your views here.
def cool(request):
    return render(request, 'cool/cool.html')