from child.models import Member
from django import template
register = template.Library()

@register.filter(name='filter')
def filter(t):
	return Member.objects.filter(id=t).count()

#@register.filter(name='add1')
#def add1():
#	return Member.objects.all().count()