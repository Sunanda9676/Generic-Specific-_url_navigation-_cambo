from django.shortcuts import render

# Create your views here.
def sql(request):
    return render(request,'sql.html')
def web(request):
    return render(request,'web.html')