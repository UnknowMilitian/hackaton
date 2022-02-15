from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(TurnirAuth)
admin.site.register(TurnirQuestion)
admin.site.register(Contact)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_display_links = ['name', ]
    prepopulated_fields = {'slug':('name',)}


class TurnirsTimeAdmin(admin.TabularInline):
    model = TurnirsTime

@admin.register(Turnir)
class TurnirAdmin(admin.ModelAdmin):
    inlines = [TurnirsTimeAdmin]


class TadbirTimeAdmin(admin.TabularInline):
    model = TadbirsTime

@admin.register(Tadbir)
class TadbirAdmin(admin.ModelAdmin):
    inlines = [TadbirTimeAdmin]