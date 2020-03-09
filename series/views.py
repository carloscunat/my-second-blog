from django.shortcuts import render,get_object_or_404,redirect
from .models import Serie
from datetime import date
from .forms import SerieForm

def series2020():
    series=Serie.objects.all()


def series_vistas():
    series=Serie.objects.all()
    count=0
    for serie in series:
        count+=1
    return count

def temporadas_vistas():
    series=Serie.objects.all()
    count=0
    for serie in series:
        count+=int(serie.temporadas)
    return count
def finalizados():
    series=Serie.objects.all()
    f=0
    for serie in series:
        if serie.finalizado == True:
            f+=1
    return f
def series_list(request):
    series=Serie.objects.all()


    info=[series_vistas(),temporadas_vistas(),finalizados()]
    return render(request, 'series/series_list.html', {'series':series,'info':info})
def serie_new(request):
    if request.method == "POST":
        form = SerieForm(request.POST)
        if form.is_valid():
            serie = form.save(commit=False)


            serie.save()
            return redirect('series_list')

    else:
        form = SerieForm()
    return render(request, 'series/serie_edit.html', {'form': form})
def serie_edit(request, serie):
    serie2 = get_object_or_404(Serie,serie=serie)
    if request.method == "POST":
        form = SerieForm(request.POST, instance=serie2)
        if form.is_valid():
            serie2 = form.save(commit=False)


            serie2.save()
            return redirect('series_list')
    else:
        form = SerieForm(instance=serie2)
    return render(request, 'series/serie_edit.html', {'form': form})
