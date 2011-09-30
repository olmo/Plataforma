from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.template import RequestContext

def index(request):
    lista = User.objects.all()
    return render_to_response('usuarios/index.html', {'lista': lista})
	
def detail(request, user_id):
    p = get_object_or_404(User, pk=user_id)
    return render_to_response('usuarios/detail.html', {'usuario': p})

def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
    return HttpResponseRedirect('/peliculas/')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/peliculas/')

def registro(request):
    try:
        apartado = int(request.POST['apartado'])
    except :
        apartado = 0

    if apartado == 1:
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.save()
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)
        return HttpResponseRedirect('/peliculas/')
    else:
        return render_to_response('usuarios/registro.html', context_instance=RequestContext(request))