from django.contrib import admin
from .models import Termo
from .models import Area
from .models import SubArea
from .models import Sugestao
from usuarios.models import Usuario

# Register your models here.

class TermoAdmin(admin.ModelAdmin):
    list_display = ('termo', 'subarea', 'expressao', 'aprovado')
    list_filter = ('aprovado', 'subarea', )
    list_editable = ('aprovado', )

class SubAreaAdmin(admin.ModelAdmin):
    list_display = ('subarea', 'area')


class SugestaoAdmin(admin.ModelAdmin):
    list_display = ('termo', 'usuario', 'timestamp')

admin.site.register(Termo, TermoAdmin)
admin.site.register(Area)
admin.site.register(SubArea, SubAreaAdmin)
admin.site.register(Sugestao, SugestaoAdmin)
