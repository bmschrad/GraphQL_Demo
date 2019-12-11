from graphene import ObjectType, String, Boolean, ID, Field, Int, List
from resource import providers, provider_products, provider_users, users_log
import json

class Products(ObjectType):
    uid = Int()
    provider_uid = Int()
    product_name = String()
    start_of_service = String()
    end_of_service = String()
    added_on = String()


class Logs(ObjectType):
    uid = Int()
    user_uid = Int()
    login_time = String()


class Users(ObjectType):
    uid = Int()
    provider_uid = Int()
    username = String()
    first_name = String()
    last_name = String()
    email = String()
    logs = List(Logs)

    def resolve_logs(self, info, **args):
        return list(filter(lambda x: x['user_uid'] == self['uid'], users_log))


class Providers(ObjectType):
    uid = Int()
    provider_name = String()
    mds_fac_id = String()
    npi = String()
    street_address = String()
    city = String()
    state = String()
    zip = String()
    products = List(Products)
    users = List(Users)

    def resolve_products(self, info, **args):
        return list(filter(lambda x: x['provider_uid'] == self['uid'], provider_products))

    def resolve_users(self, info, **args):
        return list(filter(lambda x: x['provider_uid'] == self['uid'], provider_users))


class Query(ObjectType):
    providers = List(Providers, uid=Int(required=False))
    hello = String(description="Hello")

    def resolve_providers(self, info, **args):
        if 'uid' in args:
            # User is asking for just one facility
            return list(filter(lambda x: x['uid'] == args['uid'], providers))

        # Facility not specified return all
        return providers

    def resolve_hello(self, info, **args):
        return "World"
