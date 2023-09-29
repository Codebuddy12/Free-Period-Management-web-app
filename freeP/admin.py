from django.contrib import admin

# Register your models here.
from .models import Days
from .models import Period
from .models import Details

admin.site.register(Period)
admin.site.register(Days)
admin.site.register(Details)