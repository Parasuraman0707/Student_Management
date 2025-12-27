from fastapi import FastAPI, status, HTTPException
from jose import JWTError, jwt
# pip install python-jose
# from pydantic import BaseModel
from datetime import datetime, timedelta

SECRET_KEY = "student_login"
ALGORITHM = "HS256"


def get_token(user):
    expire = datetime.utcnow() + timedelta(minutes=15)
    data = {
        'email': user,
        'from': 'GFG',
        'exp': expire
    }

    # data = {
    #     "sub": str(user_id),       # subject (user ID)
    #     "username": username,
    #     "role": role,
    #     "iat": datetime.utcnow(),  # issued at
    #     "exp": expire,             # expiration
    #     "iss": "MyApp",            # issuer
    # }
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return {encoded_jwt}

def verify_token(authorization):
    try:
        payload = jwt.decode(authorization, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )