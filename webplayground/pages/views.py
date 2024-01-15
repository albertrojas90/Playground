from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
#en termino de funciones seria asi
#def pages(request):
#    pages = get_list_or_404(Page)
#    return render(request, 'pages/pages.html', {'pages':pages})

#convirtiendolo en listas basadas en clases se veria asi
class PageListView(ListView):
    model = Page



#def page(request, page_id, page_slug):
#    page = get_object_or_404(Page, id=page_id)
#    return render(request, 'pages/page.html', {'page':page})

class PageDetailView(DetailView):
    model=Page