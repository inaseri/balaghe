from .models import Language,Translator,Content,Section
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS,fields

class LanguageResouce(ModelResource):
    class Meta:
        queryset = Language.objects.all()
        resource_name = 'language'
        filtering = {
            'title': ALL,
        }
        allowed_methods = ['get', 'post']
        include_resource_uri = False

class TranslatorResouce(ModelResource):
    class Meta:
        queryset = Translator.objects.all()
        resource_name = 'translator'
        filtering = {
            'title': ALL,
        }
        allowed_methods = ['get', 'post']
        include_resource_uri = False


class ContentResouce(ModelResource):
    class Meta:
        queryset = Content.objects.all()
        resource_name = 'content'
        filtering = {
            'id': ALL,
            'translator': ALL,
            'type': ALL,
            'title_Ar': ALL,
            'title_En': ALL,
        }
        allowed_methods = ['get', 'post']
        include_resource_uri = False


class SectionResouce(ModelResource):
    content = fields.ForeignKey(ContentResouce, 'content', full=True)
    class Meta:
        queryset = Section.objects.all()
        resource_name = 'section'
        filtering = {
            'subtitle_fa': ALL,
            'subtitle_ar': ALL,
            'body_fa': ALL,
            'body_ar': ALL,
            'description_fa': ALL,
            'description_ar': ALL,
            'content': ALL_WITH_RELATIONS,
        }
        allowed_methods = ['get', 'post']
        include_resource_uri = False