from django.shortcuts import render
from .models import Movie
from imdb import IMDb
from urllib.parse import urlparse
import json
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.
def home_view(request):
     url=request.POST.get("url")
     if url:
        url=urlparse(url)
        urls=url.path
        idd=''.join(i for i in urls if i.isdigit())
        ia = IMDb()
        movie = ia.get_movie(idd)
        title = movie.get('title')
        summary = movie.get('plot')
        director = movie.get('director')
        mv_drctr = []
        for dr in director:
            if str(dr)=='':
                pass
            else:
                mv_drctr.append(str(dr))

        writer = movie.get('writers')
        mv_wrt = []
        for write in writer:
            if str(write)=='':
                pass
            else:
                mv_wrt.append(str(write))
        stars = movie.get('cast')
        mv_str =[]
        for st in stars:
            if str(st)=='':
                pass
            else:
                mv_str.append(str(st))

        ratings = movie.get('rating')
        try:
            exist= Movie.objects.get(title=title)
        except Movie.DoesNotExist:
            exist = None
        if not exist:        
            mv=Movie()
            mv.title=title
            mv.summary=summary
            mv.director=mv_drctr
            mv.writer=mv_wrt
            mv.stars=mv_str
            mv.rating=ratings
            mv.save()

    #  context={
    #     "title":title,
    #     "summary":summary,
    #     "director":director,
    #     "writer":writer,
    #     "stars":stars,
    #     "ratings":rating
    #  }
        mv_data = Movie.objects.filter(title=title).values()  # or simply .values() to get all fields
        data_list = list(mv_data)  # important: convert the QuerySet to a list object
        return JsonResponse(data_list, safe=False)
     return render(request, "web/home.html",{})     




