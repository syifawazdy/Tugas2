from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    mywatchlist = MyWatchList.objects.all()
    watched_movie = 0
    unwatched_movie = 0
    message = ""

    for movie in mywatchlist:
        if (movie.watched):
            watched_movie += 1
        else:
            unwatched_movie += 1

    if (watched_movie >= unwatched_movie):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"
    
    context = {
    'list_barang': mywatchlist,
    'nama': 'Syifa',
    'id': '2106701066',
    'message': message
    }
    return render(request, "mywatchlist.html", context)

def show_html(request):
    mywatchlist = MyWatchList.objects.all()
    watched_movie = 0
    unwatched_movie = 0
    message = ""

    for movie in mywatchlist:
        if (movie.watched):
            watched_movie += 1
        else:
            unwatched_movie += 1

    if (watched_movie >= unwatched_movie):
        message = "Selamat, kamu sudah banyak menonton!"
    else:
        message = "Wah, kamu masih sedikit menonton!"
    
    context = {
    'list_barang': mywatchlist,
    'nama': 'Syifa',
    'id': '2106701066',
    'message': message
    }
    return render(request, "mywatchlist.html", context)

# Create your views here.
def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
