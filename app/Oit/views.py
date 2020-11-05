from django.shortcuts import render, redirect
from Oit.models import Model_OIT
from Oit.forms import Model_OIT_Form

# Create your views here.

def agregar(request):  

    if request.method == "POST":  
        form = Model_OIT_Form(request.POST)  

        if form.is_valid():  
            try:  
                form.save()  

                return redirect('/mostrar')  

            except:  

                pass  
   
    else:  

        form = Model_OIT_Form()  

    return render(request,'agregar_oit.html',{'form':form})  

def mostrar(request):  

    oit = Model_OIT.objects.all()  

    return render(request,"mostrar_oit.html",
    
    {'oit':oit}
    
    )

def editar(request, id): 

    oit = Model_OIT.objects.get(id=id) 

    return render(request,'editar_oit.html',
    
    {'oit':oit}
    
    )  

def actualizar(request, id): 

    oit = Model_OIT.objects.get(id=id) 

    form = Model_OIT_Form(request.POST, instance = oit)

    if form.is_valid():  

        form.save()  

        return redirect("/mostrar")  

    return render(request, 'editar_oit.html',
    
    {'oit': oit}
    
    )

def eliminar(request, id):  

    oit = Model_OIT.objects.get(id=id) 

    oit.delete()  

    return redirect("/mostrar")  