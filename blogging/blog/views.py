# Create your views here.
from django.http import HttpResponse
from django.conf import settings

from jinja2 import Environment, FileSystemLoader, Markup
jinja = Environment(loader=FileSystemLoader(settings.TEMPLATE_DIRS), autoescape=True)

from applicati import model

base = model.createBase('./pickles').data.applications.blog

def publish(request, category=None):
  print category
  categoryName = category
  category = getattr(base.categories, categoryName)

  template = jinja.get_template('blog/entry.html')
  context = {
    'category': category,
  }
  return HttpResponse(template.render(**context))
