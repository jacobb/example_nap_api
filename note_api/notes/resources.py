from nap import ResourceModel, Field


class Note(ResourceModel):

    title = Field(default='new title')
    content = Field()

    pk = Field(api_name='id', resource_id=True)

    class Meta:
        root_url = 'http://127.0.0.1:8000/api/v1/'
        resource_name = 'note'

    def handle_create_response(self, response):
        super(Note, self).handle_create_response(response)
        if not response.content:
            self.refresh()
