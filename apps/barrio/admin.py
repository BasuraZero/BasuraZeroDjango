from django.contrib import admin
from .models import Barrio
from .models import Calle
from .models import Hora
from .models import Dia


admin.site.register(Barrio)
admin.site.register(Calle)
admin.site.register(Hora)
admin.site.register(Dia)