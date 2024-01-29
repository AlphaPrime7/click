#Advanced click: https://click.palletsprojects.com/en/5.x/api/
#https://realpython.com/python-click/
from click import pass_context
from functools import update_wrapper


def decorator(f, object_type):
    @pass_context
    def new_func(ctx, *args, **kwargs):
        obj = ctx.find_object(object_type)
        return ctx.invoke(f, obj, *args, **kwargs)
    update_wrapper(new_func, f)
    
    return decorator