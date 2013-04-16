from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields

from notes.models import Note, Author


class AuthorResource(ModelResource):
    class Meta:
        queryset = Author.objects.all()
        resource_name = 'author'
        authentication = Authentication()
        authorization = Authorization()


class NoteResource(ModelResource):

    author = fields.ForeignKey(AuthorResource, 'author', null=True)

    class Meta:
        queryset = Note.objects.all()
        resource_name = 'note'
        authentication = Authentication()
        authorization = Authorization()
