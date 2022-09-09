import jsonschema
from flask import request

import errors


async def validate(source: str, req_schema: dict):
    """Валидатор входящих запросов"""

    async def decorator(func):

        async def wrapper(*args, **kwargs):
            try:
                jsonschema.validate(
                    instance=getattr(request, source), schema=req_schema,
                )
            except jsonschema.ValidationError as e:
                raise errors.BadRequest(e.message)

            result = func(*args, **kwargs)

            return result
        return wrapper
    return decorator
