from django.contrib import admin

from marketing.models import Cliente, Asesore, BolsaInmobiliaria, Telefono

class BolsaInline(admin.TabularInline):
	model = BolsaInmobiliaria
	extra = 1

class TelefonoInline(admin.TabularInline):
	model = Telefono
	extra = 1

class ClienteAdmin(admin.ModelAdmin):
	search_fields = ['nombre','apellido_paterno']

class AsesorAdmin(admin.ModelAdmin):
	search_fields = ['nombre']
	list_display = ('completo','email')
	inlines = [TelefonoInline]

class BolsaAdmin(admin.ModelAdmin):
	list_filter = ['fecha_registro']
	search_fields = ['descripcion','ubicacion']

# Para mostrar en el site Admin los atributos
# > list_display = ('completo','email','telefono_1')

# Para mostrar el campo 'x' veces en una relacion
# > inlines = [BolsaInline]

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Asesore, AsesorAdmin)
admin.site.register(BolsaInmobiliaria, BolsaAdmin)
