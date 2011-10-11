from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from correos.models import Mensaje
from correos.forms import CorreoForm
from django.http import Http404
from usuarios.models import Usuario
from django.contrib.auth.models import User
from django.conf.urls.defaults import url
from datetime import date

def index(request):
	try:
		lista = Mensaje.objects.filter(receptor = Usuario(request.user)).all()
	except Mensaje.DoesNotExist:
		return render_to_response('correos/index.html', context_instance=RequestContext(request))
		
	return render_to_response('correos/index.html', {'lista': lista}, context_instance=RequestContext(request))
		
def out(request):
	try:
		lista = Mensaje.objects.filter(remitente = Usuario(request.user)).all()
	except Mensaje.DoesNotExist:
		return render_to_response('correos/out.html', context_instance=RequestContext(request))
		
	return render_to_response('correos/out.html', {'lista': lista}, context_instance=RequestContext(request))

def componer(request):

	if request.method == 'POST':
		form = CorreoForm(request.POST)
		if form.is_valid():
			m = Mensaje(remitente = Usuario.objects.get(user = request.user),
					asunto = request.POST['asunto'],
					texto = request.POST['texto'],
					fecha = date.today())
			m.save()
			m.receptor.add(Usuario.objects.get(user = User.objects.get(username = request.POST['receptor'])))
			m.save()
			return HttpResponseRedirect('/buzon')					
	else:
		form = CorreoForm()
	
	return render_to_response('correos/componer.html', {'form': form}, context_instance=RequestContext(request))
