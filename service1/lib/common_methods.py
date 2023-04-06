import logging
import inspect


def handle_response(text:str):
    stack = inspect.stack()
    calling_class = (
        stack[1][0].f_locals["self"].__class__.__name__
        if "self" in stack[1][0].f_locals
        else None
    )
    print(f"[{calling_class}] {text}")