from django.shortcuts import render

# Create your views here.

def Store_View(request):
    return render(request, 'store/store.html')