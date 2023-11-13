import requests
from generic.query_stuff import build_gql_request


def get_user_by_id(id: str):
    
    get_user = build_gql_request("getUser", id=id)
    get_user.populate_response()
    
    if get_user.is_response_ok():
        return get_user.response.json()["data"]["getUser"], "success"
    else:
        return None, "failure"
