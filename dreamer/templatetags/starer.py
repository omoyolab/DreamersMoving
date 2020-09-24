from django import template

register = template.Library()

@register.simple_tag
def review(star):
    return ['fa-star'] * int(star) + ['fa-star-o'] * (5-int(star))