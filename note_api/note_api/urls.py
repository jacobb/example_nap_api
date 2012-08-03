from django.conf.urls import patterns, include

# from cocktail.api import CocktailResource
from notes.api import NoteResource


note_resource = NoteResource()

urlpatterns = patterns('',
    (r'api/', include(note_resource.urls)),
)
