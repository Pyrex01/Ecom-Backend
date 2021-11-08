from django.shortcuts import render
# Create your views here.
def get_docs(request):
    return render(request,"docs/docs.html",{"path":request.META['HTTP_HOST']})