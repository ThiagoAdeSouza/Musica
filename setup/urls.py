
from django.contrib import admin

from django.urls import path
from django.conf.urls.static import static
from setup import settings 
from playlist.views import MusicaCreateView, MusicaDetailView, MusicaDeleteView, MusicaListView, MusicaUpdateView, PlaylistCreateView, PlaylistDetailView, PlaylistDeleteView, PlaylistListView, PlaylistUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('', PlaylistListView.as_view(), name='playlist_list'),
    path ('create/', PlaylistCreateView.as_view(), name='playlist_create'),
    path ('<int:pk>/', PlaylistDetailView.as_view(), name='playlist_detail'),
    path ('<int:pk>/delete/', PlaylistDeleteView.as_view(), name='playlist_delete'),
    path ('<int:pk>/edit/', PlaylistUpdateView.as_view(), name='playlist_update'),

    path ('musicas/', MusicaListView.as_view(), name='musica_list'),
    path ('musicas/create/', MusicaCreateView.as_view(), name='musica_create'),
    path ('musicas/<int:pk>/', MusicaDetailView.as_view(), name='musica_detail'),
    path ('musicas/<int:pk>/delete/', MusicaDeleteView.as_view(), name='musica_delete'),
    path ('musicas/<int:pk>/edit/', MusicaUpdateView.as_view(), name='musica_update'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
