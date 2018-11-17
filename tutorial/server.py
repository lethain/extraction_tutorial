import graphene
import extraction
import requests


class Website(graphene.ObjectType):
    url = graphene.String()
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()

class Query(graphene.ObjectType):
    #website = graphene.Field(Website, url=graphene.String(required=True))
    website = graphene.String(url=graphene.String(required=True))
    
    def resolve_website(self, info, url):
        print(['resolve_website', info, url])
        html = requests.get(url).text
        extracted = extraction.Extractor().extract(html, source_url=url)
        return Website(url=extracted.url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image
        )


schema = graphene.Schema(query=Query)
results = schema.execute('{ website (url: "https://lethain.com/migrations/") }')
print(results.data)
