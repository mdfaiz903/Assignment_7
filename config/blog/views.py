from django.shortcuts import render

# Create your views here.
def local_news(request):
    return render(request,'blog/bg.html')