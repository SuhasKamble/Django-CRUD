from django.shortcuts import redirect, render, HttpResponse
from .models import Info

# Create your views here.
def home(request):
    infos = Info.objects.all()
    context = { 'infos':infos }
    return render(request, "home.html", context)

def add(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        info = Info(fname=fname, lname=lname, email=email, phone=phone)
        info.save()
        return redirect('/')
    return render(request, "add.html")

def deleteData(request):
    if request.method=="POST":
        deleteId = request.POST.get('deleteId')
        Info.objects.filter(sno=deleteId).delete()
        return redirect('/')
    return HttpResponse("This is delete page")

def updateData(request):
    if request.method == "POST":
        updateId = request.POST.get('updateId')
        info = Info.objects.filter(sno=updateId).first()
        Info.objects.filter(sno=updateId).delete()
        context = { 'info':info }
        return render(request, "update.html", context)
    return HttpResponse("This is update page")

