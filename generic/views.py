from django.shortcuts import render

# Create your views here.
def python(request):
    return render(request,'python.html')

def django(request):
    return render(request,'django.html')