from django.contrib import admin
from .models import Tort, Category, StatusForOffer, StatusForProblem

# Register your models here.


class TortAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']


class StatusForOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class StatusForProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


admin.site.register(Tort, TortAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StatusForProblem, StatusForProblemAdmin)
admin.site.register(StatusForOffer, StatusForOfferAdmin)
