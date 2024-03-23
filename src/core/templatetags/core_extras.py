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

# weather
@register.inclusion_tag('core/weather.html')
def weather():
    result = {
        'location': '台北',
        'text': '未知',
        'temperature': '未知'
    }
    
    import requests
    from blog.settings import WEATHER_API_URL, WEATHER_API_KEY, WEATHER_LOCATION, WEATHER_LANGUAGE

    payload = {
        'key': WEATHER_API_KEY,
        'location': WEATHER_LOCATION,
        'language': WEATHER_LANGUAGE
    }

    r = requests.get(WEATHER_API_URL, params=payload)

    if r.status_code == 200:
        data = r.json()
        result['location'] = data['results'][0]['location']['name']
        result['text'] = data['results'][0]['now']['text']
        result['temperature'] = data['results'][0]['now']['temperature']

    return result