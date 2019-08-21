from django.contrib import admin
from .models import Termo
from .models import Area
from .models import SubArea
from .models import Sugestao

# Register your models here.
admin.site.register(Termo)
admin.site.register(Area)
admin.site.register(SubArea)
admin.site.register(Sugestao)
