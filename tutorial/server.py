import graphene
import extraction
import requests


class Website(graphene.ObjectType):
    url = graphene.String(required=True)
    title = graphene.String()
    description = graphene.String()
    image = graphene.String()

class Query(graphene.ObjectType):
    website = graphene.Field(Website)
    
    def resolve_website(self, info):
        url = info.context.get('url')        
        print(['resolve_website', info, url])
        html = requests.get(url).text
        extracted = extraction.Extractor().extract(html, source_url=url)
        return Website(url=extracted.url,
                       title=extracted.title,
                       description=extracted.description,
                       image=extracted.image
        )


schema = graphene.Schema(query=Query)
result = schema.execute("""
query getWebsite($url: URL) {
  website(url: $url) {
    url
    title
  }
}""", variables={'url': "https://lethain.com/migrations/"})

print(result)
