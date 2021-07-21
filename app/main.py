#===================== Importing FastAPI necessary packages =============
from fastapi import (
    FastAPI,
    HTTPException,
    status,
    Request,
)

from src.dependecies import authenticate_user
from src.routers import router

import base64
import binascii


#------------------ FastAPI variable ----------------------------------
app = FastAPI()


# ================ Authentication Middleware =======================
#----------- Here authentication is based on basic scheme,
#----------- another authentication, based on bearer scheme, is used throughout
#---------- the application (as decribed in FastAPI oficial documentation)
@app.middleware("http")
async def authenticate(request: Request, call_next):

#-------------------- Authentication basic scheme -----------------------------
    if "Authorization" in request.headers:
        auth = request.headers["Authorization"]
        try:
            scheme, credentials = auth.split()
            if scheme.lower() == 'basic':
                decoded = base64.b64decode(credentials).decode("ascii")
                username, _, password = decoded.partition(":")
                request.state.user = await authenticate_user(username, password)
        except (ValueError, UnicodeDecodeError, binascii.Error):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid basic auth credentials"
            )

    response = await call_next(request)
    return response

# ================= Routers inclusion from src directory ===============
app.include_router(router)