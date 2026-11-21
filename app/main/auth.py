from flask import request, g, current_app
import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from functools import wraps

def jwt_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return {"message": "Authorization header is missing."}, 401

        if not auth_header.startswith("Bearer ") or not auth_header[7:].strip():
            return {"message": "Invalid authorization header."}, 401

        token = auth_header[7:].strip()

        try:
            payload = jwt.decode(
                token,
                current_app.config["JWT_SECRET"],
                algorithms=["HS256"],
                options={"require": ["exp", "sub"]}
            )
        except ExpiredSignatureError:
            return {"message": "Token has expired."}, 401
        except InvalidTokenError:
            return {"message": "Invalid authentication token."}, 401

        try:
            user_id = int(payload.get("sub"))
        except (TypeError, ValueError):
            return {"message": "Invalid user ID in token."}, 401

        g.current_user_id = user_id

        return f(*args, **kwargs)

    return wrapper
