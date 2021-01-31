from django.template import Library


register = Library()


@register.inclusion_tag('forms/form_errors.html', name='form_errors')
def form_errors_tag(*, errors):
    return dict(errors=errors)


@register.inclusion_tag('forms/form_field.html', name='form_field')
def form_field_tag(*, field):
    return dict(field=field)
