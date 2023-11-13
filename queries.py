import requests
from generic.query_stuff import build_request


def get_user_by_id(id: str):
    
    request = build_request("getUser", id=id)
    response = request.send()
    
    if response_is_ok(response):
        return response.json()["data"]["getUser"], "success"
    else:
        return None, "failure"
