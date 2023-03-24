from django import template
from django.template import RequestContext

from ..models import MenuBar

register = template.Library()


@register.inclusion_tag('Menu/menu_pattern.html', takes_context=True)
def draw_menu(context=RequestContext, menu_name='test'):
    url_path = context.request.path
    menu = MenuBar.objects.filter(category__name=menu_name).select_related('category', 'previus_url')
    return {'menu': menu, 'menu_name': menu_name, 'url_path': url_path}
