from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(needs_autoescape=True)
@stringfilter
def add_code_tag(value, arg, autoescape=True):
    tokens = value.split()
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    #tokens[arg] = '<code>'+tokens[arg]+'</code>'
    tokens[arg] = "<strong><i><span class=text-danger>%s</span></i></strong>" % (esc(tokens[arg]))
    return mark_safe(' '.join(tokens))
    #return ' '.join(tokens)