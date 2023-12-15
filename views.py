from django.shortcuts import render
from .models import emp
import pandas as pd

# Create your views here.
def display(request):
    a=emp.objects.all()
    raw_data=pd.read_excel('Book1.xlsx')
    d=pd.DataFrame(raw_data)
    for index, row in raw_data.iterrows():
     employ_instance = emp(
        empname=row['empname'],
        designation=row['designation'],
        place=row['place'],
        salary=row['salary']
    )
    employ_instance.save()
    updated_data = emp.objects.all()
    return render(request,"a.html",{'updated_data':updated_data,'a':a})

def deleteemp(request,id):
    a=emp.objects.get(id=id)
    a.delete()
    return redirect("/display")

def editemp(request,id):
    post=emp.objects.get(id=id)
    return render(request,"update.html",{'post':post})

def updateemp(request,id):
    if(request.method=="POST"):
        empname=request.POST.get('empname')
        designation=request.POST.get('designation')
        place=request.POST.get('place')
        salary=request.POST.get('salary')
        
        post=emp.objects.get(id=id);
        post.empname=empname;
        post.designation=designation;
        post.place=place;
        post.salary=salary;
        post.save();
        return redirect("/display")
        return render(request,"update.html")


        
