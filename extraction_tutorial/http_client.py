import requests


q = """
{ 
  website(url: "https://lethain.com/migrations") {
    title
    image
    description
  }
}
"""


resp = requests.post("http://localhost:5000/", params={'query': q})
print(resp.text)
