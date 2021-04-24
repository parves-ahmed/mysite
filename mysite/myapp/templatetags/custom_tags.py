from django import template

from ..models import ProjectType

register = template.Library()


@register.simple_tag
def pr_type_id(val):
    print(val)
    return val


@register.simple_tag
def project_type(key):
    result = ProjectType.objects.filter(projects__company=key).distinct()
    print(result)
    return result
