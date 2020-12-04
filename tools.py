from typing import Callable

def validate_user_input(prompt: str, valid_responses: [str], fun: Callable = None):
    response = None
    while response not in valid_responses:
        response = input(prompt)
        if fun is not None:
            try:
                response = fun(response)
            except:
                response = None
    return response