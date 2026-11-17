from . import bp
from flask import request
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash


@bp.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200

@bp.route("/register", methods=["POST"])
def register():
    data = request.get_json(silent=True)

    if not isinstance(data, dict) or not data:
        return {
            "code": "VALIDATION_ERROR",
            "message": "Request body must contain valid JSON.",
            "field": "body"
        }, 400
    
    username = data.get("username")
    password = data.get("password")

    if username is None:
        return {
            "code": "VALIDATION_ERROR",
            "message": "Username is required.",
            "field": "username"
        }, 400
        
    if not isinstance(username, str):
        return {
            "code": "VALIDATION_ERROR",
            "message": "Username must be a string.",
            "field": "username"
        }, 400

    if not username.strip():
        return {
            "code": "VALIDATION_ERROR",
            "message": "Username cannot be empty.",
            "field": "username"
        }, 400

    if len(username) < 3 or len(username) > 80:
        return {
            "code": "VALIDATION_ERROR",
            "message": "Username must be 3-80 characters.",
            "field": "username"
        }, 400

    if password is None:
        return {
            "code": "VALIDATION_ERROR",
            "message": "Password is required.",
            "field": "password"
        }, 400

    if not isinstance(password, str):
        return {
            "code": "VALIDATION_ERROR",
            "message": "Password must be a string.",
            "field": "password"
        }, 400

    if not password.strip():
        return {
            "code": "VALIDATION_ERROR",
            "message": "Password cannot be empty.",
            "field": "password"
        }, 400

    if len(password) < 15 or len(password) > 128:
        return {
            "code": "VALIDATION_ERROR",
            "message": "Password must be 15-128 characters.",
            "field": "password"
        }, 400
    

    existing_user = User.query.filter_by(username=username).first()

    if existing_user:
        return {
            "code": "USERNAME_TAKEN",
            "message": "This username is already in use.",
            "field": "username"
        }, 409

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        password_hash=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "id": new_user.id,
        "username": new_user.username,
        "created_at": new_user.created_at.isoformat()
    }, 201

