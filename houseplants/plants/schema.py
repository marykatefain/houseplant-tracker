from houseplants.plants.models import Plant, Species
from graphene_django import DjangoObjectType
import graphene

class SpeciesType(DjangoObjectType):
    class Meta:
        model = Species

class PlantType(DjangoObjectType):
    class Meta:
        model = Plant

class PlantMutation(graphene.Mutation):
    class Arguments:
        # The input arguments for this mutation
        nick_name = graphene.String(required=True)

    # The class attributes define the response of the mutation
    plant = graphene.Field(PlantType)

    def mutate(self, info, nick_name):
        plant = Plant.objects.create(nick_name=nick_name)
        # Notice we return an instance of this mutation
        return PlantMutation(plant=plant)

class Mutation(graphene.ObjectType):
    add_plant = PlantMutation.Field()

class Query(graphene.ObjectType):
    plants = graphene.List(PlantType)
    species = graphene.List(SpeciesType)

    def resolve_plants(self, info):
        return Plant.objects.all()

    def resolve_species(self, info):
        return Species.objects.all()

schema = graphene.Schema(query=Query, mutation=Mutation)
