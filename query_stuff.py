import requests
from dataclasses import dataclass
from generic.query_strings import get_user_by_id

@dataclass
class GQLRequest:
    url: str
    query: str
    variables: dict = {}
    response: requests.Response = None

    def populate_response(self):
        """ Populate the GQLRequest's '.response' attribute."""
        response = requests.post(
            url=self.url, 
            json={
                "query": self.query, 
                "variables": self.variables
                }
            )
        self.response = response

    def is_response_ok(self):
        """Check for common response issues.

        Returns:
            bool: good is true, bad is false.
        """
        if not self.response.ok:
            return False
        
        if self.response.get("errors"):
            print("some errors!")
            return False
        
        return True


query_url_map = {
    "getUser": "https://api.mocki.io/v2/c4d7a195/graphql",
}

query_map = {
    "getUser": get_user_by_id
}

def build_gql_request(query_name, **kwargs):
    request = GQLRequest(url=query_url_map[query_name], query=query_map[query_name], variables=kwargs)
    return request