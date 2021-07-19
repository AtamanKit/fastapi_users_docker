from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext

import motor.motor_asyncio

# ================= Creating necessary variables ========================
#------------------ Token, authentication variables ---------------------
SECRET_KEY = "4ab5be85c8c56eecdd547f7831979be83de58a6768d10a314f54cda4e4d67ffe"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


#----------------- Database variables (MongoDB) --------------------------
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://Fortask:fortask@cluster0.2mvpj.mongodb.net/DarqubeTask?retryWrites=true&w=majority")
db = client.DarqubeTask