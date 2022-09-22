from django.shortcuts import render
from mywatchlist.models import DataWatchlist
from django.http import HttpResponse
from django.core import serializers

# TODO: Create your views here.

def show_mywatchlist(request):
    data_data_watchlist = DataWatchlist.objects.all()
    context = {
        'list_watchlist': data_data_watchlist,
        'name': 'Raihan Kus Putranto',
        'id': '2106703821'
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request) :
    data = DataWatchlist.objects.all()

    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = DataWatchlist.objects.all()

    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = DataWatchlist.objects.filter(pk=id)

    # Jika JSON
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    # Jika XML
    # return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")