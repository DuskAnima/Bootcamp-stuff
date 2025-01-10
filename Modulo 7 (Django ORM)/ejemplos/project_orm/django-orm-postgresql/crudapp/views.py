from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import EmpleadoForm
from .models import Empleado

def insertar_emp(request):
    if request.method == 'POST':
        emp_id = request.POST['emp_id']
        print(f"Valor recibido para emp_id: '{emp_id}' (longitud: {len(emp_id)})")
        emp_nombre = request.POST['emp_nombre']
        emp_correo = request.POST['emp_correo']
        emp_designacion = request.POST['emp_designacion']
        empleado = Empleado(emp_id=emp_id, emp_nombre=emp_nombre, emp_correo=emp_correo, emp_designacion=emp_designacion)
        empleado.save()
        return redirect('mostrar/')
    else:
        return render(request, 'insertar.html')

def mostrar_emp(request):
    empleados = Empleado.objects.all()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    context = {'empleados':empleados, 'num_visits': num_visits,}
    return render(request,'mostrar.html', context)

def editar_emp(request, pk):
    empleado = Empleado.objects.get(id=pk)
    #if request.method == 'POST':
    #    return redirect('/crudapp/mostrar')
    context = {'empleado':empleado}
    return render(request, 'editar.html', context)    

def actualizarempleado(request, id):
    emp_id = request.POST['emp_id']
    emp_nombre = request.POST['emp_nombre']
    emp_correo = request.POST['emp_correo']
    emp_designacion = request.POST['emp_designacion']
    empleado = Empleado.objects.get(id=id)
    empleado.emp_id = emp_id
    empleado.emp_nombre = emp_nombre
    empleado.emp_correo = emp_correo
    empleado.emp_designacion = emp_designacion
    empleado.save()
    return redirect(reverse('mostrar-emp'))

def eliminar_emp(request, pk):
    empleado = Empleado.objects.get(id=pk)
    if request.method == 'POST':
        empleado.delete()
        return redirect(reverse('mostrar-emp'))
    context = {'empleado' : empleado}
    return render(request, 'eliminar.html', context)

def empleado_detalle(request, pk):
    empleado = Empleado.objects.get(emp_id=pk) #al poner el nombre de la variable id, pude referirme no a su pk sino a su id de empleado
    context = {'empleado': empleado}
    return render(request, 'detalle.html', context)