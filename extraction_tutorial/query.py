import pprint
import tutorial.server


def query_url(url):
    q = '''
    { 
      website (url: "%s" ) {
        url
        title
        image
        description
      }
    }
    ''' % (url,)
    result = tutorial.server.schema.execute(url)
    if result.errors:
        raise Exception(result.errors)
    return result.data


if __name__ == "__main__":
    query_url("https://lethain.com/migrations/")
