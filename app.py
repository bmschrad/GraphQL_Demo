from flask import Flask
from flask_cors import CORS
from resource import providers, provider_products, provider_users, users_log
from schema import Query
from flask_graphql import GraphQLView
from graphene import Schema
import json
import os


view_func = GraphQLView.as_view(
    'graphql', schema=Schema(query=Query), graphiql=True)

app = Flask(__name__)
app.add_url_rule('/graphql', view_func=view_func)
CORS(app)

def keyRemove(source, keys):
    new_source = source.copy()
    for key in keys:
        del new_source[key]
    return new_source

@app.route('/providers')
def providers_list():
    return json.dumps(providers)

@app.route('/provider/<int:uid>')
def provider_info(uid):
    return json.dumps(list(filter(lambda x: x['uid'] == uid, providers)))

@app.route('/provider/<int:uid>/products')
def provider_products_list(uid):
    return json.dumps(list(filter(lambda x: x['provider_uid'] == uid, provider_products)))

@app.route('/provider/<int:uid>/users')
def provider_users_list(uid):
    return json.dumps(list(filter(lambda x: x['provider_uid'] == uid, provider_users)))

@app.route('/users/<int:uid>/logging')
def provider_users_history_list(uid):
    return json.dumps(list(filter(lambda x: x['user_uid'] == uid, users_log)))

@app.route('/provider_summary/<int:uid>')
def provider_summary(uid):
    provider = keyRemove(list(filter(lambda x: x['uid'] == uid, providers))[-1], ['npi', 'street_address', 'state'])

    products = list(filter(lambda x: x['provider_uid'] == uid, provider_products))
    new_products = []
    for product in products:
        new_products.append(keyRemove(product, ['uid', 'provider_uid', 'start_of_service', 'end_of_service']))

    users = list(filter(lambda x: x['provider_uid'] == uid, provider_users))
    new_users = []
    for user in users:
        result = keyRemove(user, ['uid', 'provider_uid', 'first_name', 'last_name', 'email', 'last_login'])
        result['login_time'] = list(filter(lambda x: x['user_uid'] == user['uid'], users_log))[-1]['login_time']
        new_users.append(result)

    provider['products'] = new_products
    provider['users'] = new_users
    return json.dumps(provider)

#test
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 5000))
