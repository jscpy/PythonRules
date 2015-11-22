from django.shortcuts import render, render_to_response, HttpResponse
from django.views.generic import TemplateView, ListView
from django.core.context_processors import csrf

from marketing.models import Cliente, Asesore, Telefono

class Menu(TemplateView):
    template_name = "menu.html"

'''
	 <<<< ------------- VIEWS CLIENTE -------------  >>>>
'''
class ClientesListView(ListView):
    model = Cliente
    template_name = "agenda/clientes_list.html"
    context_object_name = "clientes_list"

def Cliente_detalles(request,pk):
	try:
		cliente = Cliente.objects.get(pk=int(pk))
	except Exception as e:
		cliente = ""

	dict_cliente = dict(cliente = cliente,pk=pk)

	return render_to_response('agenda/cliente_detalles.html',dict_cliente)



'''
	 <<<< ------------- VIEWS ASESORES -------------  >>>>
'''
class AsesorListView(ListView):
    model = Asesore
    template_name = "asesores/asesor_list.html"
    context_object_name = "asesores_list"

def Asesor_detalles(request,pk):
	telefonos = Telefono.objects.filter(asesor_id=int(pk))
	asesor = Asesore.objects.get(pk=int(pk))

	lista_telefonos = []
	for item in telefonos:
		lista_telefonos.append(item.numero)
	
	dict_asesor = dict(asesor=asesor,lista_telefonos = lista_telefonos, pk=pk)

	return render_to_response('asesores/asesor_detalles.html',dict_asesor)
