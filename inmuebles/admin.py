from django.contrib import admin
from .models import *

admin.site.register(tipo_inmueble)
admin.site.register(operacion_inmueble)
admin.site.register(estado_inmueble)
admin.site.register(inmueble)
admin.site.register(imagenes_inmueble)
admin.site.register(inmuebles_usuario)
admin.site.register(review_inmueble)
admin.site.register(inmuebles_favoritos_usuario)
admin.site.register(inmuebles_cliente)