from tastypie import fields
from tastypie.resources import ModelResource
from italianTurkish.models import Item, Topic


class TopicResource(ModelResource):
    class Meta:
        queryset = Topic.objects.all()
        resource_name = 'topics'
        excludes = ['resource_uri']

    def alter_list_data_to_serialize(self, request, data_dict):
        data_dict['topics'] = data_dict['objects']
        del data_dict['objects']
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del (data_dict['meta'])
                return data_dict

    def alter_deserialized_list_data(self, request, data_dict):
        data_dict['objects'] = data_dict['topics']
        del data_dict['topics']
        return data_dict


class ItemResource(ModelResource):
    topic = fields.CharField(attribute="topic")

    class Meta:
        queryset = Item.objects.all()
        resource_name = 'items'
        fields = ['source', 'target', 'topic', 'id']
        excludes = ['resource_uri']

    def alter_list_data_to_serialize(self, request, data_dict):
        data_dict['items'] = data_dict['objects']
        del data_dict['objects']
        if isinstance(data_dict, dict):
            if 'meta' in data_dict:
                del (data_dict['meta'])
                return data_dict

    def alter_deserialized_list_data(self, request, data_dict):
        data_dict['objects'] = data_dict['items']
        del data_dict['items']
        return data_dict


