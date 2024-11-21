from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import D, T
from .forms import DForm, TForm
# Create your views here.

def home(request):
    return render(request, 'desarrollos/home.html')

@login_required
def proyectos(request):
    proyectos = D.objects.all()
    return render(request, 'desarrollos/proyectos.html', {'proyectos': proyectos})

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    return render(request, 'registration/register.html', data)

def crear(request):
    formulario = DForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('proyectos')
    return render(request, 'proyectoscreados/crear.html', {'formulario': formulario})

def editar(request, id):
    d = D.objects.get(id=id)
    formulario = DForm(request.POST or None, request.FILES or None, instance=d)
    if formulario.is_valid() and request.POST:
        formulario.save()
        return redirect('proyectos')
    return render(request, 'proyectoscreados/editar.html', {'formulario': formulario})

def eliminar(request, id):
    D2 = D.objects.get(id=id)
    D2.delete()
    return redirect('proyectos')

def form(request):
    return render(request, 'proyectoscreados/form.html')


################

def tickets(request):
    tickets = T.objects.all()
    return render(request, 'ticket/tickets.html', {'tickets': tickets})

def formt(request):
    return render(request, 'ticket/tickets.html')

def creart(request):
    formulario2 = TForm(request.POST or None, request.FILES or None)
    if formulario2.is_valid():
        formulario2.save()
        return redirect('tickets')
    return render(request, 'ticket/creart.html', {'formulario2': formulario2})

def editart(request, Id):
    T2 = T.objects.get(Id=Id)
    formulario2 = TForm(request.POST or None, request.FILES or None, instance=T2)
    if formulario2.is_valid() and request.POST:
        formulario2.save()
        return redirect('tickets')
    return render(request, 'ticket/editart.html', {'formulario2': formulario2})

def eliminart(request, Id):
    T2 = T.objects.get(Id=Id)
    T2.delete()
    return redirect('tickets')