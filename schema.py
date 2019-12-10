from graphene import ObjectType, String, Boolean, ID, Field, Int, List
from resource import providers
import json

class Providers(ObjectType):
    uid = Int()
    provider_name = String()
    mds_fac_id = String()
    npi = String()
    street_address = String()
    city = String()
    state = String()
    zip = String()

class Query(ObjectType):
    reviews = List(Review)
    providers = List(Providers)
    hello = String(description="Hello")

    def resolve_providers(self, info, **args):
        print(providers)
        # return json.dumps(providers)
        return providers

    def resolve_hello(self, info, **args):
        return "World"
