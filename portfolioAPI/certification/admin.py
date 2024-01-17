from django.contrib import admin
from certification.models import Certification, Badges, Language

# Register your models here.
admin.site.register(Certification)
admin.site.register(Badges)
admin.site.register(Language)