from django.shortcuts import render,get_object_or_404,redirect
from .models import Serie
from datetime import date
from .forms import SerieForm



def series_vistas(series):

    count=0
    for serie in series:
        count+=1
    return count

def temporadas_vistas(series):

    count=0
    for serie in series:
        count+=int(serie.temporadas)
    return count
def finalizados(series):

    f=0
    for serie in series:
        if serie.finalizado == True:
            f+=1
    return f
def listas(request):

    return render(request, 'series/listas.html')
def series2020(request):
    series2020=[]
    series=Serie.objects.all()
    for s in series:
        if s.visto=="2020":
            series2020.append(s)
    info=[series_vistas(series2020),temporadas_vistas(series2020),finalizados(series2020)]
    return render(request, 'series/series_list.html', {'series':series2020,'info':info})
def series2019(request):
    series2019=[]
    series=Serie.objects.all()
    for s in series:
        if s.visto=="2019":
            series2019.append(s)
    info=[series_vistas(series2019),temporadas_vistas(series2019),finalizados(series2019)]
    return render(request, 'series/series_list.html', {'series':series2019,'info':info})
def series2018(request):
    series2018=[]
    series=Serie.objects.all()
    for s in series:
        if s.visto=="2018":
            series2018.append(s)
    info=[series_vistas(series2018),temporadas_vistas(series2018),finalizados(series2018)]
    return render(request, 'series/series_list.html', {'series':series2018,'info':info})
def series_list(request):
    series=Serie.objects.all()


    info=[series_vistas(series),temporadas_vistas(series),finalizados(series)]
    return render(request, 'series/series_list.html', {'series':series,'info':info})
def serie_new(request):
    if request.method == "POST":
        form = SerieForm(request.POST)
        if form.is_valid():
            serie = form.save(commit=False)


            serie.save()
            return redirect('/')

    else:
        form = SerieForm()
    return render(request, 'series/serie_edit.html', {'form': form})
def serie_edit(request, serie,visto):
    serie2 = get_object_or_404(Serie,serie=serie,visto=visto)
    if request.method == "POST":
        form = SerieForm(request.POST, instance=serie2)
        if form.is_valid():
            serie2 = form.save(commit=False)


            serie2.save()
            return redirect('/')
    else:
        form = SerieForm(instance=serie2)
    return render(request, 'series/serie_edit.html', {'form': form})
def serie_remove(request, serie,visto):
    serie2 = get_object_or_404(Serie, serie=serie,visto=visto)
    serie2.delete()
    return redirect('/')
