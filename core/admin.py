from core.models import DescripcionRopa, TipoRopa
from django.contrib import admin

# Register your models here.

class RopaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'color','valor', 'stock' , 'talla', 'grupoRopa']
    search_fields = [ 'nombre', 'talla']
    list_filter = ['grupoRopa']
    list_per_page = 5

admin.site.register(TipoRopa)
admin.site.register(DescripcionRopa, RopaAdmin)

