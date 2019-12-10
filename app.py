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

#test
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 5000))
