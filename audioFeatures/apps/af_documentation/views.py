from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage

from af_documentation.models import Section

def home(request):

    return render(request,
                  'af_documentation/home.html',
                  {
                      'nodes': Section.objects.all(),
                  })






###Helpers###
def paginate(list, request):
    p = Paginator(list, 5)
    page = request.GET.get('page')
    try:
        list = p.page(page)
    except EmptyPage:
        list = p.page(p.num_pages)
    except:
        list = p.page(1)

    return list