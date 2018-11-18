import pprint
import extraction_tutorial.schema


def query_url(url):
    q = """
    {
      website (url: "https://lethain.com/migrations/" ) {
        url
        title
        image
      }
    }
    """
    result = extraction_tutorial.schema.schema.execute(q)
    if result.errors:
        if len(result.errors) == 1:
            raise Exception(result.errors[0])
        else:
            raise Exception(result.errors)
    return result.data


if __name__ == "__main__":
    results = query_url("https://lethain.com/migrations/")
    pprint.pprint(results)
