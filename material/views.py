from django.shortcuts import render_to_response
from django.template import RequestContext
from material.forms import FiltroForm
from django.utils import simplejson
from django.http import HttpResponse
from material.models import Examen
from material.admin import ExamenForm

def index(request):
    filtro = FiltroForm()
    return render_to_response('material/index.html', {'filtro':filtro}, context_instance=RequestContext(request))

def add(request):
    try:
        apartado = int(request.POST['apartado'])
    except :
        apartado = 0

    if apartado == 0:
        form = ExamenForm()
        return render_to_response('material/add.html', {'form':form, 'apartado': apartado}, context_instance=RequestContext(request))

    elif apartado == 1:
        request.POST['estado'] = 'P'
        f = ExamenForm(request.POST, request.FILES)
        f.save()
        return render_to_response('material/add.html', {'apartado': apartado}, context_instance=RequestContext(request))

def select_ajax(request):
    id = request.GET['id']
    examenes = Examen.objects.filter(asignatura=id)
    l = list()
    for examen in examenes:
        if examen.convocatoria == 'S':
            conv = 'Septiembre'
        elif examen.convocatoria == 'F':
            conv = 'Febrero'
        elif examen.convocatoria =='D':
            conv = 'Diciembre'
        elif examen.convocatoria =='J':
            conv = 'Junio'
        l.append({'id':examen.id, 'anno':examen.anno, 'convocatoria':conv, 'solucion':examen.solucion, 'archivo':examen.archivo.url})

    json = simplejson.dumps(l, ensure_ascii=False)
    return HttpResponse(json, mimetype='application/javascript')