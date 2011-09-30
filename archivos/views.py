from django.shortcuts import render_to_response
from django.template import RequestContext
from archivos.forms import FiltroForm
from django.utils import simplejson
from django.http import HttpResponse
from archivos.models import Examen
from archivos.admin import ExamenForm

def index(request):
    filtro = FiltroForm()
    return render_to_response('archivos/index.html', {'filtro':filtro}, context_instance=RequestContext(request))

def add(request):
    try:
        apartado = int(request.POST['apartado'])
    except :
        apartado = 0

    if apartado == 0:
        form = ExamenForm()
        return render_to_response('archivos/add.html', {'form':form, 'apartado': apartado}, context_instance=RequestContext(request))

    elif apartado == 1:
        e = Examen()
        f = ExamenForm(request.POST, request.FILES, instance=e)
        f.save()
        return render_to_response('archivos/add.html', {'apartado': apartado}, context_instance=RequestContext(request))

def select_ajax(request):
    id = request.GET['id']
    examenes = Examen.objects.filter(id=id)
    l = list()
    for examen in examenes:
        if examen.convocatoria == 'S':
            conv = 'Septiembre'
        elif examen.convocatoria == 'F':
            conv = 'Febrero'
        elif examen.convocatoria =='D':
            conv = 'Diciembre'
        l.append({'id':examen.id, 'anno':examen.anno, 'convocatoria':conv, 'solucion':examen.solucion, 'archivo':examen.archivo.url})

    json = simplejson.dumps(l, ensure_ascii=False)
    return HttpResponse(json, mimetype='application/javascript')