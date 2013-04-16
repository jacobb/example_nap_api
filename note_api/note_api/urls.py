from django.conf.urls import patterns, include

from tastypie.api import Api

from notes.api import NoteResource, AuthorResource

v1_api = Api(api_name='v1')
v1_api.register(NoteResource())
v1_api.register(AuthorResource())


urlpatterns = patterns('',
    (r'api/', include(v1_api.urls)),
)
