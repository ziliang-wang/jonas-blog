from django import template
from taggit.models import Tag

register = template.Library()


@register.filter(name='to_str')
def int_to_str(value):
    return str(value)


@register.filter(name='highlight')
def highlight_title(text, search):
    if search:
        text = text.replace(search, f'<span class="bg-secondary text-white">{ search }</span>')
    return text

# hot tags
@register.inclusion_tag('core/tags.html')
def display_tags():
    tags = Tag.objects.all()

    return {
        'tags': tags
    }