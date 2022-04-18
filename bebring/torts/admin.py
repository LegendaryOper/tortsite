from django.contrib import admin
from .models import Tort, Category, StatusForOffer, StatusForProblem, TortPhoto, Offer, Problem

# Register your models here.


class TortPhotoInline(admin.TabularInline):
    fk_name = 'product'
    model = TortPhoto


class TortAdmin(admin.ModelAdmin):
    list_display = ['name', 'cost']
    inlines = [TortPhotoInline,]


class StatusForOfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class StatusForProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']


class OfferAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']


class ProblemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status']
    readonly_fields = ['name','image_tag', 'phone_number', 'tort', 'description']
    fields = ['name', 'status', 'description', 'tort', 'image_tag', 'phone_number']


admin.site.register(Tort, TortAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(StatusForProblem, StatusForProblemAdmin)
admin.site.register(StatusForOffer, StatusForOfferAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Problem, ProblemAdmin)

