from graphene import ObjectType, String, Boolean, ID, Field, Int, List
from resource import review_json, providers
from json2obj import json2obj
import json

class User(ObjectType):
    first_name = String()
    has_profile_pic = Boolean()
    id = ID()
    picture_url = String()
    smart_name = String()
    thumbnail_url = String()

class Listing(ObjectType):
    id = ID()
    name = String()

class Review(ObjectType):
    author = Field(User)
    author_id = ID()
    can_be_edited = Boolean()
    comments = String()
    created_at = String()
    id = Int()
    language = String()
    listing = Field(Listing)
    listing_id = ID()
    recipient = Field(User)
    recipient_id = ID()
    response = String()
    role = String()
    user_flag = Boolean()

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

    def resolve_reviews(context, info):
                # reviews = api_call(args.get("id"))["reviews"]
                # breakpoint()
                reviews = review_json['reviews'][-1]
                print(reviews)
                # return json2obj(json.dumps(reviews))
                # return json2obj(reviews)
                return json.dumps(reviews)

    def resolve_providers(self, info, **args):
        print(providers)
        # return json.dumps(providers)
        return providers

    def resolve_hello(self, info, **args):
        return "World"
