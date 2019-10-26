from django.contrib import admin

# Register your models here.
from .models import Evento
admin.site.register(Evento)

from .models import Servicio
admin.site.register(Servicio)

from .models import Proveedore
admin.site.register(Proveedore)

from .models import Producto
admin.site.register(Producto)

from .models import Cliente
admin.site.register(Cliente)

from .models import MiEvento
admin.site.register(MiEvento)





