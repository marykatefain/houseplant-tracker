from houseplants.plants.models import Plant
from graphene_django import DjangoObjectType
import graphene

class PlantType(DjangoObjectType):
    class Meta:
        model = Plant

class Query(graphene.ObjectType):
    plants = graphene.List(PlantType)

    def resolve_plants(self, info):
        return Plant.objects.all()

schema = graphene.Schema(query=Query)
