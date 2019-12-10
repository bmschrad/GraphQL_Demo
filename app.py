from flask import Flask
from flask_cors import CORS
from resource import providers
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
def provider(uid):
    return json.dumps(list(filter(lambda x: x['uid'] == uid, providers)))

@app.route('/provider/<int:uid>/products')
def provider_products(uid):
    return 'products'
    #  return json.dumps(list(filter(lambda x: x['uid'] == uid, providers)))

#test
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 5000))
