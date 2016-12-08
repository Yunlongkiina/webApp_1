

from .models import Album
# Create your views here
from django.shortcuts import render, get_object_or_404


def index(request):
    all_albums = Album.objects.all()
    """
        html=''
    for album in all_albums:
        url = '/music/' + str(album.id) + '/'
        html += '<a href="'+url+'">' + album.album_title +'</a><br>'
    """


    return render(request,'music/index.html',{'all_albums': all_albums})


def details(request, album_id):

    """

    try:
       album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404("Albummdoes not exist. ")

    """
    album = get_object_or_404(Album, id = album_id)

    return render(request,'music/detail.html',{'album':album})



