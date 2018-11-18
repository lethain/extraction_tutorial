
This repository is an Example project using [Graphene](https://graphene-python.org/)
and [flask-graphql]() to create a [GraphQL]()
server and client pair in Python.

The specific

https://github.com/lethain/extraction

Queries against the server look like:

    {
      website(url: "https://lethain.com/migrations") {
        title
	image
	description
      }
    }

And responses look like:

    {
      "data": {
        "website": {
	  "title":"Migrations: the sole scalable fix to tech debt.",
	  "image":"https://lethain.com/static/blog/2018/migrations-hero.png",
	  "description":"Migrations are both essential and frustratingly frequent as your codebase ages and your business grows: most tools and processes only support about one order magnitude of growth before becoming ineffective, so rapid growth makes them a way of life. This post takes a look at why migrations are so important, and also how to run them effectively."
	}
      }
    }

Take a look at the `extraction_tutorial` directory for more.

## Setup

    git clone git@github.com:lethain/extraction_tutorial.git
    cd extraction_tutorial
    python3 -m venv env
    . ./env/bin/activate
    pip install -r requirements.txt
    pip install -e .
    python extraction_tutorial/server.py &
    python extraction_tutorial/http_client.py


