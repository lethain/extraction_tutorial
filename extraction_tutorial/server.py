import graphene
import extraction
import requests



class Website(graphene.ObjectType):
    url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()

class Query(graphene.ObjectType):
    website = graphene.Field(Website, url=graphene.String())

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

result = schema.execute('''
{ 
  website (url: "https://lethain.com/migrations/" ) {
    url
    title
    image
  }
}

''')

if result.errors:
    print(result.errors)
else:
    pprint.pprint(result.data)
