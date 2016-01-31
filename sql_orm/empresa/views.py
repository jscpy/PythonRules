from django.shortcuts import render, render_to_response
from django.views.generic import TemplateView, ListView, View
from django.http import HttpResponse
from django.template import Template, Context

from io import BytesIO
from rlextra.rml2pdf import rml2pdf

from empresa.models import Empleado, Departamento

class Index(TemplateView):
	template_name = "index.html"

class EmpleadoListView(ListView):
	model = Empleado
	template_name = "empleado_list.html"
	context_object_name = "empleados"
	
	queryset = Empleado.objects.values('clave','nombre','apellidos',
	'departamento__nombre','departamento__presupuesto')


def pdfgen(request):
	name = 'Jesus'
	last_name = 'Solis'

	path_rml = 'rml/hello.rml'
	t = Template(open(path_rml,'r').read())
	c = Context(
		{"name":name,"last_name":last_name}
	)
	rml = t.render(c)
	rml.encode('utf8')

	#print(rml)

	buf = BytesIO()
	rml2pdf.go(rml,outputFileName=buf)
	pdfData = buf.getvalue()
	buf.close()

	response = HttpResponse(content_type='application/pdf')
	response.write(pdfData)
	response['Content-Disposition'] = 'attachment; filename="ficha.pdf"'

	
	# p = canvas.Canvas(buffer)
	# p.drawString(250, 250, "Hello world.")
	# p.showPage()
	# p.save()
	# pdf = buffer.getvalue()
	# buffer.close()
	# response.write(pdf)
	
	return response