from django.shortcuts import render,get_object_or_404,redirect
from .models import Serie
from django.utils import timezone
from .forms import SerieForm

def series_list(request):
    series=Serie.objects.all()
    return render(request, 'series/series_list.html', {'series':series})
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
