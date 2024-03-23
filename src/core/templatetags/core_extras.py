from django import template
from taggit.models import Tag

register = template.Library()


@register.filter(name='to_str')
def int_to_str(value):
    return str(value)


# hot tags
@register.inclusion_tag('core/tags.html')
def display_tags():
    tags = Tag.objects.all()

    return {
        'tags': tags
    }