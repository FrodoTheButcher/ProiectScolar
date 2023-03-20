from django.contrib import admin
from .models import Profile  ,Kids, motivari_elev  , absente_elev
# Register your models here.
admin.site.register(Profile)
admin.site.register(Kids)
admin.site.register(motivari_elev)
admin.site.register(absente_elev)



