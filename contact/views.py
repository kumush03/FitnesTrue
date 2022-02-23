from django.http import HttpResponseRedirect
from django.shortcuts import render
from contact.models import Contact
from django.shortcuts import HttpResponseRedirect
# Create your views here.

def fitnes(request):
    data = Contact.objects.all()
    return render(request,'index.html',{'data':data})


def sendMessages(request):
    if request.method == "POST":
        sendMessage = Contact()
        sendMessage.name = request.POST.get("name")
        sendMessage.email = request.POST.get("email") 
        sendMessage.address = request.POST.get("address") 
        sendMessage.message = request.POST.get("message") 
        sendMessage.save()
        return HttpResponseRedirect('/')
