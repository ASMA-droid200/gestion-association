from django.shortcuts import render, get_object_or_404, redirect
from .models import Materiel

def dashboard(request):
    total_materiels = Materiel.objects.count()

    return render(request, 'dashboard.html', {
        'total_materiels': total_materiels
    })


def materiels_list(request):
    materiels = Materiel.objects.all()
    return render(request, 'materiels/materiels.html', {'materiels': materiels})


def materiel_detail(request, id):
    materiel = get_object_or_404(Materiel, id=id)
    return render(request, 'materiels/materiel_detail.html', {'materiel': materiel})


def ajouter_materiel(request):
    if request.method == "POST":
        nom = request.POST['nom']
        type_m = request.POST['type']
        quantite = request.POST['quantite']
        description = request.POST['description']

        Materiel.objects.create(
            nom=nom,
            type=type_m,
            quantite=quantite,
            description=description
        )

        return redirect('/materiels/')

    return render(request, 'materiels/ajouter_materiel.html')