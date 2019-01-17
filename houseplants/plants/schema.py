from houseplants.plants.models import Plant, Species
from graphene_django import DjangoObjectType
import graphene

class SpeciesType(DjangoObjectType):
    class Meta:
        model = Species

class PlantType(DjangoObjectType):
    class Meta:
        model = Plant

class Query(graphene.ObjectType):
    plants = graphene.List(PlantType)
    species = graphene.List(SpeciesType)

    def resolve_plants(self, info):
        return Plant.objects.all()

    def resolve_species(self, info):
        return Species.objects.all()

schema = graphene.Schema(query=Query)
