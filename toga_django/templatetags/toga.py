import os

from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.filter
def html(widget):
    return mark_safe(widget.__html__())


@register.inclusion_tag('toga_django/toga_head_js.html', takes_context=True)
def toga_head_js(context):
    return context


@register.inclusion_tag('toga_django/toga_body_js.html')
def toga_body_js():
    return {}