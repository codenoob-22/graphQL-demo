import graphene
from graphene import ObjectType

import ingredients.schema

class Query(ingredients.schema.ParentQuery, ObjectType):
# will inherit from multiple queries
    pass

schema = graphene.Schema(query=Query)