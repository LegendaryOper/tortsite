from ..models import Category
from django import template
from django.db.models import *

register = template.Library()


@register.inclusion_tag('torts/categories_list.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}
