import graphene
from graphene_django import DjangoObjectType

from hero.models import Hero

class HeroType(DjangoObjectType):
    class Meta:
        model = Hero


class Query(graphene.ObjectType):
    heroes = graphene.List(HeroType)

    def resolve_heroes(self, info, **kwargs):
        return Hero.objects.all()
