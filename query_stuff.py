import requests
from dataclasses import dataclass
from generic.query_strings import get_user_by_id

@dataclass
class GQLRequest:
    url: str
    query: str
    variables: dict = {}

    def send(self):
        response = requests.post(
            url=self.url, 
            json={
                "query": self.query, 
                "variables": self.variables
                }
            )
        return response


query_url_map = {
    "getUser": "https://api.mocki.io/v2/c4d7a195/graphql",
}

query_map = {
    "getUser": get_user_by_id
}

def build_request(query_name, **kwargs):
    request = GQLRequest(url=query_url_map[query_name], query=query_map[query_name], variables=kwargs)
    return request