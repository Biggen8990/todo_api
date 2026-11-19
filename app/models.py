from app.extensions import db
from datetime import datetime, timezone
from werkzeug.security import check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    
    def check_password(self, candidate):
        return check_password_hash(self.password_hash, candidate)
