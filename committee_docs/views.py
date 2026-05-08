from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Document

def documents_list(request):
    pvs = Document.objects.filter(type_doc='pv')
    pdfs = Document.objects.filter(type_doc='pdf')

    return render(request, 'committee_docs/documents.html', {
        'pvs': pvs,
        'pdfs': pdfs
    })

