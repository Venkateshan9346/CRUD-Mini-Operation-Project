from django.shortcuts import render,redirect
from guviapp.models import Register
def home(request):
    query=Register.objects.all()
    context={"data":query}
    return render(request, 'home.html',context)
def register(request):
    query=Register.objects.all()
    context={"data":query}   
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get("email")
        age=request.POST.get("age")
        course=request.POST.get("course")
        query=Register(name=fullname,email=email,age=age,course=course)
        query.save()
    return render(request, 'home.html',context)

def update(request,id):
    if request.method=="POST":
        fullname=request.POST.get('fullname')
        email=request.POST.get("email")
        age=request.POST.get("age")
        course=request.POST.get("course")
        edit=Register.objects.get(id=id)
        edit.name=fullname
        edit.email=email
        edit.age=age
        edit.course=course
        edit.save()
        return redirect("/")
    
    data=Register.objects.get(id=id)
    context={"data":data}
    return render(request,"update.html",context)

def deletedata(request,id):
    data=Register.objects.get(id=id)
    data.delete()
    return redirect('/')
