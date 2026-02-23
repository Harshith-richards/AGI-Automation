from datetime import datetime, timedelta, timezone
import jwt
from passlib.context import CryptContext
from ..config import get_settings

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
settings = get_settings()


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)


def create_token(sub: str, minutes: int | None = None) -> str:
    exp = datetime.now(timezone.utc) + timedelta(minutes=minutes or settings.access_token_minutes)
    return jwt.encode({'sub': sub, 'exp': exp}, settings.jwt_secret, algorithm=settings.jwt_algorithm)
