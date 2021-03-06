from rest_framework.fields import CharField, IntegerField
from rest_framework.serializers import ModelSerializer

from market.models import Category, Product


class SubCategoryModelSerializer(ModelSerializer):
    code = CharField()
    name = CharField()

    class Meta:
        model = Category
        fields = ('code', 'name')


class CategoryModelSerializer(ModelSerializer):
    code = CharField()
    name = CharField()
    sub_categories = SubCategoryModelSerializer(many=True)

    class Meta:
        model = Category
        fields = ('code', 'name', 'sub_categories')
