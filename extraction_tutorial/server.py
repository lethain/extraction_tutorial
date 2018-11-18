"""
Python HTTP server for GraphQL.
"""
from flask import Flask
from flask_graphql import GraphQLView
from extraction_tutorial.schema import schema


app = Flask(__name__)
app.add_url_rule('/', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))
app.run()
