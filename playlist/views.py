from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from playlist.forms import MusicaForm, PlaylistForm
from playlist.models import Musica, Playlist 

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist/playlist_list.html'
    context_object_name= 'playlists'
    paginate_by = 8
    queryset= Playlist.objects.order_by("-id")

class PlaylistDetailView(DetailView):
    model = Playlist
    template_name = 'playlist/playlist_detail.html'

class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistUpdateView(UpdateView):
    model = Playlist
    fields = ['nome', 'musicas']  
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')  

class PlaylistDeleteView(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist_list')  

# musicas crud

class MusicaListView(ListView):
    model = Musica
    template_name = 'musicas/musica_list.html'

class MusicaDetailView(DetailView):
    model = Musica
    template_name = 'musicas/musica_detail.html'

class MusicaCreateView(CreateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'musicas/musica_form.html'
    success_url = reverse_lazy('musica_list')

class MusicaUpdateView(UpdateView):
    model = Musica
    form_class = MusicaForm
    template_name = 'musicas/musica_form.html'
    success_url = reverse_lazy('musica_list')  

class MusicaDeleteView(DeleteView):
    model = Musica
    template_name = 'musicas/musica_confirm_delete.html'
    success_url = reverse_lazy('musica_list')