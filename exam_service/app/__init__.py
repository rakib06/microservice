import logging
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from .routers import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = "django-insecure-rzk1s_i3dro$f513(&^=-tgpc7t2%l$+vb6qj6b&%(=or*#awk"
ALGORITHM = "HS256"

# Enable logging
logging.basicConfig(level=logging.INFO)

def verify_token(token: str = Depends(oauth2_scheme)):
    logging.info(f"Received token: {token}")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        logging.info(f"Decoded token payload: {payload}")
        username: str = payload.get("username")
        if username is None:
            raise HTTPException(status_code=403, detail="Invalid credentials")
        return username
    except JWTError as e:
        logging.error(f"Token validation error: {e}")
        raise HTTPException(status_code=403, detail="Invalid token")

app.include_router(router, dependencies=[Depends(verify_token)])
