from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import BlogPost
from .models import EquipmentCategory,EquipmentItem
from django.forms import TextInput, Textarea
from django.db import models

class EquipmentItemAdmin(admin.ModelAdmin):
    formfield_overrides = {

        models.CharField: {'widget': TextInput(attrs={'size':'100'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

    list_display = ('product_name', 'description','price')


admin.site.register(EquipmentItem, EquipmentItemAdmin)
admin.site.register(BlogPost)
admin.site.register(EquipmentCategory)

